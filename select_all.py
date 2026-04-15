from db import get_cursor

def select_all():
    conn, cursor = get_cursor()
    
    try:
        sql = "SELECT seq, name, id, subject, score, semester, regdate FROM student"
        cursor.execute(sql)
        rows = cursor.fetchall()

        print("\n--- [ 성적 전체 목록 ] ---")
        print("번호 | 이름(ID)    | 과목명            | 점수 | 학기   | 등록일")
        print("-----------------------------------------------------------")

        for row in rows:
            seq = row[0]
            name = row[1]
            user_id = row[2]
            subject = row[3]
            score = row[4]
            semester = row[5]
            regdate = row[6]

            # 포맷 맞춰 출력
            print(f"{seq:<4} | {name}({user_id}) | {subject:<15} | {score:<4} | {semester:<6} | {regdate}")

        print("-----------------------------------------------------------")

    except Exception as e:
        print("조회 실패:", e)

    finally:
        cursor.close()
        conn.close()