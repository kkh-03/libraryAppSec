from db import get_cursor

def select_all():
    conn, cursor = get_cursor()
    
    try:
        sql = "SELECT id_grade, m.id, m.name, subject, score, term, reg_date FROM grades g " \
        "JOIN member m ON g.member_seq = m.seq;"
        cursor.execute(sql)
        rows = cursor.fetchall()

        if not rows:
            print("해당 학생이 없습니다.")
            return

        print("\n--- [ 성적 전체 목록 ] ---")
        print("번호 | 이름(ID)    | 과목명            | 점수 | 학기   | 등록일")
        print("-----------------------------------------------------------")

        for row in rows:
            id_grade = row[0]
            user_id = row[1]
            name = row[2]
            subject = row[3]
            score = row[4]
            term = row[5]
            reg_date = row[6]

            # 포맷 맞춰 출력
            print(f"{id_grade:<4} | {name}({user_id}) | {subject:<15} | {score:<4} | {term:<6} | {reg_date}")

        print("-----------------------------------------------------------")

    except Exception as e:
        print("조회 실패:", e)

    finally:
        cursor.close()
        conn.close()