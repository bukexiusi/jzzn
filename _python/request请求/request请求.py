import requests, json

def main():
    # params = {
    #     'data_type': "1",
    #     'task_id': '6f54b774-4b9f-11e9-b9f4-b888e37aee1e',
    #     'ids': ['af838ac2-4c4a-11e9-bb83-b888e37aee1e']
    # }
    # result = requests.post("http://localhost:8000/cs/datable/get/table/data/by/id", json=params)
    # result_json = json.loads(result.text)
    # case = result_json.get("data")
    # if len(case) == 0:
    #     raise Exception("can not find case data")
    # case = case[0]
    # print("jz")
    data = {
        "数据表名": "zn_business_table_10",
        "id": "124269127421396992",
        "执行时长": 123,
        "执行说明": "成功",
        "案号": "12"
    }
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        raise Exception("传入类型错误")
    result = requests.post(
        "http://{}:{}/table/data/save/data".format("140.4.18.195", "8000"),
        json=data,
        timeout=10)
    print(result)


def main1():
    resp = requests.get(
        "http://{}:{}/table/data/get/full/data/by/id".format("localhost", "8000"),
        {"data_id": "125199836180908039", "table_name": "zn_business_table_0"},
        timeout=10)

    if not resp:
        raise Exception("网络原因，获取数据失败")

    if resp.status_code != 200:
        raise Exception("后端异常")
    data = json.loads(resp.text)
    return data

if __name__ == "__main__":
    main1()
