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
