# MianShiTi

#### 创建本地仓库

- git init                           将当前目录变为一个git可以管理的本地仓库
- git add filename/.       将文件添加到本地仓库中
- git status                      查看提交状态
- git commit -m ''           将文件提交到本地仓库中

#### 将本地仓库和远程仓库进行合并

1.  ssh-keygen -t rsa -C "[youremail@example.com](mailto:youremail@example.com)"           生成公有密钥文件 

2.  git remote add origin  git@github.com:virsing/Leetcode.git      将本地仓库和远程仓库关联起来

   ```py
   1. git push -u origin master                         第一次提交且远程仓库为空
   2. git pull --rebase origin master                   远程仓库已有readmd.md文件
      git push origin master
   ```

### 版本回退

- git log 查看历史纪录
- git log –pretty=oneline 以一行显示历史纪录
- git reset --hard HEAD^ 回退到上一个版本
- git reset --hard HEAD^^ 回退到上上一个版本
- git reset --hard HEAD~n 回退到前n个版本
- git reflog 获取版本号
- git reset --hard 6fcfc89 以版本号恢复被回退的版本

#### 其他常用命令

- git diff fileName 查看文件前后的变化

- git fetch origin 从主分支拉下最新版本

- git merge origin/master 将本地最新版本合并到主分支

  