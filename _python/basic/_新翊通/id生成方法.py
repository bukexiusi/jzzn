'''
snowflake是twitter开源的分布式ID生成算法，其核心思想是：产生一个long型的ID，使用其中41bit作为毫秒数，10bit作为机器编号，12bit作为毫秒内序列号。
这个算法单机每秒内理论上最多可以生成1000*(2^12)个，也就是大约400W的ID，完全能满足业务的需求。
'''

import sys
import random
import threading
import time

from concurrent import futures

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance


class Snowflake(metaclass=SingletonType):
    # 区域标识
    region_id_bits = 2
    # 机器标识
    worker_id_bits = 10
    # 序列号标识
    sequence_bits = 11

    MAX_REGION_ID = -1 ^ (-1 << region_id_bits)
    MAX_WORKER_ID = -1 ^ (-1 << worker_id_bits)
    SEQUENCE_MASK = -1 ^ (-1 << sequence_bits)

    WORKER_ID_SHIFT = sequence_bits
    REGION_ID_SHIFT = sequence_bits + worker_id_bits
    TIMESTAMP_LEFT_SHIFT = (sequence_bits + worker_id_bits + region_id_bits)

    def __init__(self, worker_id=1, region_id=0):
        self.twepoch = 1549728000000
        self.last_timestamp = -1
        self.sequence = 0

        assert 0 <= worker_id <= Snowflake.MAX_WORKER_ID
        assert 0 <= region_id <= Snowflake.MAX_REGION_ID

        self.worker_id = worker_id
        self.region_id = region_id

        self.lock = threading.Lock()

    def generate(self, bus_id=None):
        return self.next_id(
            True if bus_id is not None else False,
            bus_id if bus_id is not None else 0
        )

    def next_id(self, is_padding, bus_id):
        with self.lock:
            timestamp = self.get_time()
            padding_num = self.region_id

            if is_padding:
                padding_num = bus_id

            if timestamp < self.last_timestamp:
                try:
                    raise ValueError(
                        'Clock moved backwards. Refusing to'
                        'generate id for {0} milliseconds.'.format(
                            self.last_timestamp - timestamp
                        )
                    )
                except ValueError:
                    print(sys.exc_info[2])

            if timestamp == self.last_timestamp:
                self.sequence = (self.sequence + 1) & Snowflake.SEQUENCE_MASK
                if self.sequence == 0:
                    timestamp = self.tail_next_millis(self.last_timestamp)
            else:
                self.sequence = random.randint(0, 9)

            self.last_timestamp = timestamp

            return (
                    (timestamp - self.twepoch) << Snowflake.TIMESTAMP_LEFT_SHIFT |
                    (padding_num << Snowflake.REGION_ID_SHIFT) |
                    (self.worker_id << Snowflake.WORKER_ID_SHIFT) |
                    self.sequence
            )

    def tail_next_millis(self, last_timestamp):
        timestamp = self.get_time()
        while timestamp <= last_timestamp:
            timestamp = self.get_time()
        return timestamp

    def get_time(self):
        return int(time.time() * 1000)


def main():
    snowflake = Snowflake(1)
    snowflake2 = Snowflake(1)
    _id = str(snowflake.generate())
    print(_id)
    print(len(_id))
    _id = str(snowflake.generate())
    print(_id)

# def main():
#     id_set = set()
#     snowflake = Snowflake(1)
#
#     def gen_id():
#         try:
#             _id = snowflake.generate()
#         except Exception as e:
#             print(e)
#         else:
#             assert _id not in id_set
#             id_set.add(_id)
#
#     with futures.ThreadPoolExecutor(max_workers=16) as executor:
#         futs = [executor.submit(gen_id) for _ in range(100)]
#
#     print('{0} IDs in the set'.format(len(id_set)))
#     print(*id_set, sep='\n')


if __name__ == '__main__':
    main()