from db import get_cursor

def select_one():
    conn, cursor = get_cursor()
    
    try:
        student_seq = int(input("조회할 학생 번호(seq) 입력: "))
        cursor.execute("SELECT id FROM student WHERE seq = %s", (student_seq,))
        result = cursor.fetchone()

        user_id = result[0]

        sql = """SELECT name, id, subject, score, semester FROM student
        WHERE id = %s"""
        cursor.execute(sql, (user_id,))
        rows = cursor.fetchall()

        if not rows:
            print("해당 학생이 없습니다.")
            return

        
        name = rows[0][0]
        user_id = rows[0][1]
        semester = rows[0][4]
    
        print(f"\n--- [ {name} 학생의 성적 리포트 ] ---")
        print(f"- 아이디: {user_id}")
        print(f"- 학기: {semester}")
        print("-------------------------------------")

        total = 0

        for i, row in enumerate(rows, start = 1):
            subject = row[2]
            score = row[3]
            total += score
            print(f"{i}. {subject}: {score}점")

        average_score = total / len(rows)

        print("-----------------------------")
        print(f"평균 점수 : {average_score:.1f}점")


    except Exception as e:
        print("조회 실패:", e)

    finally:
        cursor.close()
        conn.close()