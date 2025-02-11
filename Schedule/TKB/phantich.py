def parse_schedule(text):
    lines = text.strip().split('\n')
    schedule = {}
    for line in lines:
        if 'Thứ' not in line:
            continue
        parts = line.split('\t')
        if len(parts) > 1:
            course_id = parts[1]
            schedule[course_id] = {
                'course_name': parts[2],
                'credits': parts[3],
                'instructor': parts[6],
                'schedule': parts[7],
                'weeks': parts[8]
            }
    for course_id, details in schedule.items():
        details['schedule'] = parse_schedule_tag(details['schedule'])
    return schedule
def parse_schedule_tag(schedule_tag):
    parts = schedule_tag.split(',')
    day = int(parts[0].split()[1])
    periods = list(map(int, parts[1].split('-')))
    room = parts[2] 
    return [day] + periods + [room]
    
colors = [
"#ADD8E6",
"#90EE90",
"#F08080",
"#FAFAD2",
"#FFB6C1",
"#FFA07A",
"#87CEFA",
"#B0C4DE",
"#FFFFE0",
"#AFEEEE",
]
if __name__ == '__main__':
    t = """
    TT	Thông tin lớp học phần	Khảo sát ý kiến cuối học kỳ
    Mã lớp học phần	Tên lớp học phần	Số TC	Tích hợp	CLC	Giảng viên	Thời khóa biểu	Tuần học	Đề cương	Công thức điểm	DSSV	Học lại	Bắt đầu	Kết thúc	Hạn hiện điểm	Hoàn thành
    1	4130120.2420.24.45	Anh văn B1.1	3			Trần Thị Thanh Nhã	Thứ 6,1-4,H201	29-40								
    2	0130221.2420.24.06	B24-GDTC2-BC-06	0			Khoa G.dục thể chất - ĐHĐN	Thứ 5,1-4,GDTC	29-44								
    3	1023280.2420.24.12	Cấu trúc dữ liệu	2			Đặng Thiên Bình	Thứ 4,6-7,H105	29-44								
    4	1022970.2420.24.11	Cấu trúc máy tính và vi xử lý	2			Bùi Thị Thanh Thanh	Thứ 3,6-7,H104	29-44								
    5	3190121.2420.24.06	Giải tích 2	4			Trần Văn Sự	Thứ 3,1-4,H302	29-44								
    6	1022933.2420.24.12B	PBL1: Dự án lập trình tính toán	2			Nguyễn Thị Minh Hỷ	Thứ 7,1-2,H104	29-44								
    7	1020072.2420.24.12	Phương pháp tính	3			Đỗ Thị Tuyết Hoa	Thứ 6,8-10,H106	29-44								
    8	1021263.2420.24.12	Toán rời rạc	3			Nguyễn Văn Hiệu	Thứ 4,8-10,H105	29-44								
    9	3050011.2420.24.27	Vật lý 1	3			Mai Thị Kiều Liên	Thứ 4,1-3,H108	29-44			
    """
    schedule_dict = parse_schedule(t)
    print(schedule_dict)