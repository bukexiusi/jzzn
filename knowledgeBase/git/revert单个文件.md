# revert单个文件

1. 进入文件所在目录

    ```git
    git log Demo.java
    ```

2. 回退到指定版本

    ```git
    git reset b47eeeaa048c0bf5ce707df2086170942a2e7233 Demo.java
    ```

3. 提交到本地（注意不要git add）

    ```git
    git commit -m "revert"
    ```

4. 更新到工作目录

    ```git
    git checkout Demo.java
    ```
