import jpype

# jvmPath = jpype.getDefaultJVMPath()
# jvmPath = r'C:\Program Files\Java\jre1.8.0_191\bin\server\jvm.dll'
# jpype.startJVM(jvmPath)
# jpype.java.lang.System.out.println("hello world!")


# jvmPath = r'C:\Program Files\Java\jre1.8.0_191\bin\server\jvm.dll'
# jpype.startJVM(jvmPath, r"-Djava.class.path=C:\work\aes-for-python-1.0-SNAPSHOT.jar")
# main = jpype.JClass('com.yidao.Main')
# content = 'dUhlJ1n1ZSidgieQpKED1UIcdHx+/lxPJJiM8QO1X3dEZe/hei9jbprMiB3EbPeIrO5zJTJCij15TXLGgQBvfA=='
# key = 's1V2eRAWWy3Zq+p/mGuCZGmO0Qj/m2XV6GLokgx0LSU='
# message = main.decryptAES(content, key)
# jpype.shutdownJVM()
# message_list = message.split(',')
# print(message_list)


jpype.startJVM(jpype.getDefaultJVMPath(), "-ea", r"-Djava.class.path=C:\work\aes-for-python-1.0-SNAPSHOT.jar")
main = jpype.JClass('com.yidao.Main')
content = 'dUhlJ1n1ZSidgieQpKED1UIcdHx+/lxPJJiM8QO1X3dEZe/hei9jbprMiB3EbPeIrO5zJTJCij15TXLGgQBvfA=='
key = 's1V2eRAWWy3Zq+p/mGuCZGmO0Qj/m2XV6GLokgx0LSU='
message = main.decryptAES(content, key)
jpype.shutdownJVM()
message_list = message.split(',')
print(message_list)