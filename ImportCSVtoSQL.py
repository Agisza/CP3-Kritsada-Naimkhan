import pandas as pd
import pyodbc
import numpy as np

# อ่านไฟล์ CSV
csv_file_path = '@'
df_csv = pd.read_csv(csv_file_path)

# สร้างการเชื่อมต่อกับ SQL Server
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=@;'
    'DATABASE=@;'
    'UID=@;'
    'PWD=@;'
)
cursor = conn.cursor()

# แสดงข้อมูลบางส่วนจากไฟล์ CSV เพื่อการตรวจสอบ
print("Data from CSV file:")
print(df_csv.head())

# แทนที่ค่าค่าว่าง (NaN) ด้วยค่าเริ่มต้น เช่น ค่าว่าง (Empty String) หรือ 0 สำหรับคอลัมน์ที่เป็น float
df_csv = df_csv.fillna({
    'ProblemName': '',
    'ProblemDes': '',
    'Problem1': '',
    'Problem2': '',
    'Problem3': '',
    'Problem4': '',
    'Problem5': '',
    'Cause1': '',
    'Cause2': '',
    'Cause3': '',
    'Cause4': '',
    'Cause5': '',
    'RealProblem': '',
    'RealProblemType': '',
    'CounterMeasure': '',
    'RealCause': '',
    'RealCauseType': '',
    'PermanentAction': '',
    'SimilarProblem': '',
    'Xstandard': '',
    'Xknown': '',
    'Yknown': '',
    'Xfollow': '',
    'Yfollow': '',
    'MistakeType': '',
    'XUser': '',
    'YUser': '',
    'CreateDate': '',
    'UserCreate': 0,
    'BatchNo': 0,
    'CaseID': ''
})

# แปลงรูปแบบวันที่ให้เป็นรูปแบบที่ SQL Server ยอมรับได้
df_csv['CreateDate'] = pd.to_datetime(df_csv['CreateDate'], dayfirst=True, errors='coerce').dt.strftime('%Y-%m-%d %H:%M:%S')

# สร้างคำสั่ง SQL UPDATE สำหรับแต่ละแถวในไฟล์ CSV
for index, row in df_csv.iterrows():
    update_query = f"""
    UPDATE QC_ProblemAnalysisData
    SET ProblemName = ?,
        ProblemDes = ?,
        Problem1 = ?,
        Problem2 = ?,
        Problem3 = ?,
        Problem4 = ?,
        Problem5 = ?,
        Cause1 = ?,
        Cause2 = ?,
        Cause3 = ?,
        Cause4 = ?,
        Cause5 = ?,
        RealProblem = ?,
        RealProblemType = ?,
        CounterMeasure = ?,
        RealCause = ?,
        RealCauseType = ?,
        PermanentAction = ?,
        SimilarProblem = ?,
        Xstandard = ?,
        Xknown = ?,
        Yknown = ?,
        Xfollow = ?,
        Yfollow = ?,
        MistakeType = ?,
        XUser = ?,
        YUser = ?,
        CreateDate = ?,
        UserCreate = ?
    WHERE BatchNo = ? AND CaseID = ?
    """
    cursor.execute(update_query, row['ProblemName'], row['ProblemDes'], row['Problem1'], row['Problem2'], 
                   row['Problem3'], row['Problem4'], row['Problem5'], row['Cause1'], row['Cause2'], 
                   row['Cause3'], row['Cause4'], row['Cause5'], row['RealProblem'], row['RealProblemType'], 
                   row['CounterMeasure'], row['RealCause'], row['RealCauseType'], row['PermanentAction'], 
                   row['SimilarProblem'], row['Xstandard'], row['Xknown'], row['Yknown'], row['Xfollow'], 
                   row['Yfollow'], row['MistakeType'], row['XUser'], row['YUser'], row['CreateDate'], 
                   row['UserCreate'], row['BatchNo'], row['CaseID'])

# บันทึกการเปลี่ยนแปลงและปิดการเชื่อมต่อ
conn.commit()
cursor.close()
conn.close()
