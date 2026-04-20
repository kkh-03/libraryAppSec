from db import get_cursor

def select_one():
    conn, cursor = get_cursor()
    
    try:
        student_seq = int(input("조회할 학생 번호(seq) 입력: "))
        cursor.execute("SELECT id, name FROM member WHERE seq = %s", (student_seq,))
        result = cursor.fetchone()

        user_id = result[0]
        name = result[1]

        cursor.execute("""SELECT subject, score, term FROM grades
        WHERE member_seq = %s""", (student_seq,))
        rows = cursor.fetchall()

        if not rows:
            print("해당 학생이 없습니다.")
            return

        term = rows[0][2]
    
        print(f"\n--- [ {name} 학생의 성적 리포트 ] ---")
        print(f"- 아이디: {user_id}")
        print(f"- 학기: {term}")
        print("-------------------------------------")

        total = 0

        for i, row in enumerate(rows, start = 1):
            subject = row[0]
            score = row[1]
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