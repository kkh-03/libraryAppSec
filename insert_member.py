from db import get_cursor

def insert_member():
    conn, cursor = get_cursor()

    try:
        print("--- [ 성적 데이터 추가] ---")

        student_seq = int(input("- 학생 번호(seq) 입력:  "))
        cursor.execute("SELECT name, id FROM member WHERE seq = %s", (student_seq,))
        rows = cursor.fetchone()

        if not rows:
            print("해당 학생이 없습니다.")
            return
        
        name = rows[0]
        user_id = rows[1] 
        

        subject_input = input("- 과목명 입력:")
        score_input = int(input("- 점수 입력: "))
        term_input = input("- 학기 입력(예: 2026-1):")

        sql = """INSERT INTO grades (member_seq, subject, score, term, reg_date) VALUES (%s, %s, %s, %s, NOW())"""
                

        cursor.execute(sql, ( student_seq, subject_input, score_input, term_input))
        
        conn.commit()
        
        print(f"[시스템] {name} 학생의 {subject_input} 성적이 성공적으로 등록되었습니다.")


    except Exception as e:
        print("조회 실패:", e)

    finally:
        cursor.close()
        conn.close()
