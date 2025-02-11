from PIL import Image, ImageDraw, ImageFont
import phantich
import random

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
def draw_text_with_max_width(draw, text, position, font, max_width, fill):
    lines = []
    words = text.split()
    while words:
        line = ''
        while words and draw.textbbox((0, 0), line + words[0], font=font)[2] <= max_width:
            line = line + (words.pop(0) + ' ')
        lines.append(line)
    
    y = position[1]
    for line in lines:
        draw.text((position[0] + 20, y), line, font=font, fill=fill)
        y += draw.textbbox((0, 0), line, font=font)[3]
def generator(t):
    image_path = 'tbk.png'
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("SVN-Segoe UI.ttf", 40, encoding="utf-8")
    max_width = 340  # Set your max width here
    position = (513, 385)
    tkb = phantich.parse_schedule(t)
    def add_course(course):
        text = course['course_name'] + '\n' + str(course['schedule'][3] ) 
        cpos = (position[0] + (course['schedule'][0] - 2) * 64 * 6, position[1] + (course['schedule'][1] - 1) * 128)
        rect_x0 = cpos[0]
        rect_y0 = cpos[1]
        rect_x1 = cpos[0] + 384
        rect_y1 = cpos[1] + (course['schedule'][2] - course['schedule'][1] + 1) * 128
        draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], outline="black", fill=random.choice(phantich.colors), width=4)
        draw_text_with_max_width(draw, text, cpos, font, max_width, fill=(0, 0, 0))
    for course in tkb.values():
        add_course(course)
    return image