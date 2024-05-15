# Abaqus commands

## 显示abaqus信息

- `abaqus info=system`

## 验证子程序

- `abaqus verify -user_std`

## 生成inp文件

- `abaqus cae noGUI=abqmodel.py`

## 提交命令

- `abaqus input = inpname.inp job=Jobname user=umat.for cpus=8 memory=8000mb ask=off int`

## 后处理

- `abaqus python postprocess_file.py`  


# Powershell commands

## 查询命令路径

- `where` in  `win cmd`
  - `where abaqus`
- `where.exe` in `powershell`
  - `where.exe abaqus`
- `Get-Command` in `powershell`
  - `Get-Command where*`

## 执行脚本中的命令
1. 以管理员身份打开 PowerShell 输入 `set-executionpolicy remotesigned`，并输入`Y`。打开执行脚本权限
1. 将命令写入后缀名为`ps1`的文本文件
1. `cd` 进入文件所在目录
1. 输入`.\filename.ps1`执行文件中的命令
