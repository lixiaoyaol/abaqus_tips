# abaqus commands

## 验证子程序

- `abaqus verify -user_std`

## 生成inp文件

- `abaqus cae noGUI=abqmodel.py`

## 提交命令

- `abaqus input = inpname.inp job=Jobname user=umat.for cpus=8 memory=8000mb ask=off int`

## 后处理

- `abaqus python postprocess_file.py`
