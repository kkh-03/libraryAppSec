from db import get_cursor

def insert_member():
    conn, cursor = get_cursor()

    try:
        print("--- [ 성적 데이터 추가] ---")

        student_seq = int(input("- 학생 번호(seq) 입력:  "))
        cursor.execute("SELECT name, id FROM student WHERE seq = %s", (student_seq,))
        rows = cursor.fetchone()

        if not rows:
            print("해당 학생이 없습니다.")
            return
        
        name = rows[0]
        user_id = rows[1] 
        

        subject_input = input("- 과목명 입력:")
        score_input = int(input("- 점수 입력: "))
        semester_input = input("- 학기 입력(예: 2026-1):")

        sql = """INSERT INTO student (name, id, subject, score, semester, regdate) VALUES (%s, %s, %s, %s, %s, NOW())"""
                
        # 3. 쿼리 실행
        cursor.execute(sql, (name, user_id, subject_input, score_input, semester_input))
        
        # 4. 데이터베이스 반영 (INSERT/UPDATE/DELETE 작업 시 필수!)
        conn.commit()
        
        print(f"[시스템] {name} 학생의 {subject_input} 성적이 성공적으로 등록되었습니다.")


    except Exception as e:
        print("조회 실패:", e)

    finally:
        cursor.close()
        conn.close()
