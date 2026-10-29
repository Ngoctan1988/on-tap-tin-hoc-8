import streamlit as st
import time
import random
from datetime import datetime

# Cấu hình trang web
st.set_page_config(
    page_title="AI Learning Hub - Kiểm Tra Tin Học 8",
    page_icon="💻",
    layout="centered"
)

# Giao diện CSS hiện đại, phong cách AI & Thân thiện với học sinh THCS
st.markdown("""
    <style>
    .main { background-color: #f0f4f8; }
    .stButton>button { 
        width: 100%; 
        border-radius: 12px; 
        font-weight: bold; 
        background: linear-gradient(135deg, #0066cc, #00c6ff); 
        color: white; 
        border: none;
        padding: 0.6rem;
        box-shadow: 0 4px 6px rgba(0, 102, 204, 0.2);
    }
    .stButton>button:hover { 
        background: linear-gradient(135deg, #004080, #0099cc); 
    }
    h1 { color: #0f172a; text-align: center; font-weight: 800; }
    .ai-banner {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .user-card {
        background: white;
        padding: 15px 20px;
        border-radius: 10px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# NGÂN HÀNG CÂU HỎI (20 CÂU CHO MỖI CHỦ ĐỀ)
MASTER_QUESTIONS = {
    "Chủ đề 1: Máy tính và cộng đồng": [
        {"id": 1101, "level": "Dễ", "type": "trắc nghiệm", "question": "Năm 1642, nhà bác học người Pháp nào đã chế tạo chiếc máy tính cơ học đầu tiên mang tên Pascaline?", "options": ["Gottfried Leibniz", "Blaise Pascal", "Charles Babbage", "Howard Aiken"], "answer": "Blaise Pascal", "explanation": "Blaise Pascal chế tạo máy Pascaline năm 1642 để giúp cha tính thuế."},
        {"id": 1102, "level": "Dễ", "type": "đúng sai", "question": "Nhà toán học Charles Babbage được coi là 'cha đẻ' của công nghệ máy tính nhờ thiết kế máy tính đa năng tự động.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Nguyên lí thiết kế của Babbage là nền tảng cho máy tính hiện đại."},
        {"id": 1103, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thành phần điện tử chính của máy tính thế hệ thứ ba (1965-1974) là gì?", "options": ["Đèn điện tử chân không", "Bóng bán dẫn", "Mạch tích hợp (IC)", "Vi xử lí VLSI"], "answer": "Mạch tích hợp (IC)", "explanation": "Thế hệ thứ ba sử dụng các mạch tích hợp IC giúp giảm kích thước."},
        {"id": 1104, "level": "Trung bình", "type": "trả lời ngắn", "question": "Công nghệ tạo nên bộ vi xử lí thế hệ thứ tư với mật độ siêu cao viết tắt là gì? (Viết hoa)", "answer": "VLSI", "explanation": "VLSI (Very Large Scale Integration) là công nghệ vi xử lí hiện đại."},
        {"id": 1105, "level": "Dễ", "type": "trắc nghiệm", "question": "Thiết bị nào sau đây đánh dấu sự ra đời của máy tính điện tử thế hệ thứ nhất?", "options": ["ENIAC", "Pascaline", "Altair 8800", "IBM PC"], "answer": "ENIAC", "explanation": "ENIAC ra đời năm 1946 là máy tính điện tử số lớn đầu tiên."},
        {"id": 1106, "level": "Dễ", "type": "trắc nghiệm", "question": "Bộ vi xử lí (CPU) đầu tiên trên thế giới do hãng nào chế tạo vào năm 1971?", "options": ["Microsoft", "Intel", "Apple", "IBM"], "answer": "Intel", "explanation": "Intel đã cho ra mắt chip vi xử lí 4004 vào năm 1971."},
        {"id": 1107, "level": "Trung bình", "type": "trắc nghiệm", "question": "Đặc trưng cơ bản của máy tính điện tử thế hệ thứ hai là gì?", "options": ["Sử dụng đèn chân không", "Sử dụng bóng bán dẫn (Transistor)", "Sử dụng mạch tích hợp", "Sử dụng trí tuệ nhân tạo"], "answer": "Sử dụng bóng bán dẫn (Transistor)", "explanation": "Thế hệ thứ hai thay thế đèn chân không bằng bóng bán dẫn từ khoảng năm 1958."},
        {"id": 1108, "level": "Dễ", "type": "đúng sai", "question": "Trí tuệ nhân tạo (AI) là công nghệ đang được tích hợp ngày càng mạnh mẽ vào các hệ thống máy tính hiện đại.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "AI giúp máy tính có khả năng học tập, suy nghĩ và giải quyết vấn đề như con người."},
        {"id": 1109, "level": "Trung bình", "type": "trắc nghiệm", "question": "Internet bắt nguồn từ dự án mạng nào trước đây?", "options": ["ARPANET", "MILNET", "NSFNET", "EUNET"], "answer": "ARPANET", "explanation": "ARPANET do Bộ Quốc phòng Mỹ phát triển là tiền thân của Internet ngày nay."},
        {"id": 1110, "level": "Dễ", "type": "trắc nghiệm", "question": "Thiết bị thông minh nào dưới đây kết hợp giữa điện thoại di động và máy tính cá nhân?", "options": ["SmartPhone", "Máy tính để bàn", "Máy in", "Loa thùng"], "answer": "SmartPhone", "explanation": "Điện thoại thông minh tích hợp đầy đủ tính toán và liên lạc linh hoạt."},
        {"id": 1111, "level": "Trung bình", "type": "trắc nghiệm", "question": "Cuộc cách mạng công nghiệp lần thứ tư gắn liền với công nghệ chủ đạo nào?", "options": ["Động cơ hơi nước", "Điện năng và dây chuyền", "Công nghệ thông tin và Internet vạn vật (IoT, AI)", "Năng lượng hạt nhân"], "answer": "Công nghệ thông tin và Internet vạn vật (IoT, AI)", "explanation": "Cách mạng công nghiệp 4.0 lấy kỹ thuật số, AI và IoT làm trọng tâm."},
        {"id": 1112, "level": "Dễ", "type": "đúng sai", "question": "Máy tính bảng (Tablet) có thể xem là một dạng máy tính cá nhân thu gọn với màn hình cảm ứng.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Máy tính bảng có cấu trúc tương tự laptop nhưng tối ưu tính cơ động bằng cảm ứng."},
        {"id": 1113, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thiết bị nào sau đây dùng để kết nối các mạng máy tính khác nhau với nhau?", "options": ["Router (Bộ định tuyến)", "Switch", "Hub", "Cáp quang"], "answer": "Router (Bộ định tuyến)", "explanation": "Router chịu trách nhiệm định tuyến gói tin giữa các mạng khác nhau."},
        {"id": 1114, "level": "Dễ", "type": "trắc nghiệm", "question": "Hệ điều hành nào phổ biến nhất trên điện thoại thông minh hiện nay bên cạnh iOS?", "options": ["Windows", "Android", "Linux", "MS-DOS"], "answer": "Android", "explanation": "Android do Google phát triển chiếm thị phần lớn trên thiết bị di động."},
        {"id": 1115, "level": "Trung bình", "type": "trắc nghiệm", "question": "Đâu là ưu điểm lớn nhất của điện toán đám mây (Cloud Computing)?", "options": ["Phải mua ổ cứng dung lượng lớn", "Lưu trữ và truy xuất dữ liệu mọi lúc, mọi nơi qua Internet", "Chỉ dùng được khi không có mạng", "Không bao giờ bị mất dữ liệu"], "answer": "Lưu trữ và truy xuất dữ liệu mọi lúc, mọi nơi qua Internet", "explanation": "Điện toán đám mây giúp linh hoạt truy cập tài nguyên qua mạng Internet."},
        {"id": 1116, "level": "Dễ", "type": "đúng sai", "question": "Dữ liệu lớn (Big Data) đòi hỏi các công cụ phân tích truyền thống để xử lý.", "options": ["Đúng", "Sai"], "answer": "Sai", "explanation": "Big Data có khối lượng khổng lồ nên cần công nghệ xử lý chuyên biệt, không thể dùng công cụ truyền thống."},
        {"id": 1117, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thiết bị nào trong nhà thông minh (Smart Home) giúp tự động hóa việc bật tắt đèn?", "options": ["Cảm biến chuyển động và công tắc thông minh", "Ổ cắm cơ", "Quạt điện cơ", "Bóng đèn sợi đốt cũ"], "answer": "Cảm biến chuyển động và công tắc thông minh", "explanation": "Hệ thống IoT tích hợp cảm biến để tự động hóa không gian sống."},
        {"id": 1118, "level": "Dễ", "type": "trắc nghiệm", "question": "Đâu là thành phần không thể thiếu của một hệ thống máy tính cá nhân?", "options": ["Màn hình, Thân máy, Bàn phím, Chuột", "Máy in màu", "Máy chiếu", "Kính thực tế ảo"], "answer": "Màn hình, Thân máy, Bàn phím, Chuột", "explanation": "Đây là các thiết bị cơ bản tối thiểu để tương tác với máy tính cá nhân."},
        {"id": 1119, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thiết bị số nào hỗ trợ người khiếm thị đọc văn bản thông qua công nghệ chuyển đổi văn bản thành giọng nói?", "options": ["Phần mềm đọc màn hình và AI hỗ trợ", "Máy nghe nhạc cassette", "Tivi thường", "Đèn bàn học"], "answer": "Phần mềm đọc màn hình và AI hỗ trợ", "explanation": "Công nghệ số hỗ trợ hòa nhập cộng đồng cho người khuyết tật rất hiệu quả."},
        {"id": 1120, "level": "Dễ", "type": "đúng sai", "question": "Sử dụng máy tính liên tục nhiều giờ liền mà không nghỉ ngơi có hại cho sức khỏe mắt và cột sống.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Cần duy trì tư thế đúng và thời gian hợp lý khi sử dụng thiết bị số."}
    ],
    "Chủ đề 2: Tổ chức lưu trữ, tìm kiếm và trao đổi thông tin": [
        {"id": 1201, "level": "Dễ", "type": "trắc nghiệm", "question": "Đặc điểm nào sau đây KHÔNG phải của thông tin số?", "options": ["Dễ dàng nhân bản và lan truyền", "Lưu trữ dung lượng khổng lồ", "Tuyệt đối an toàn và luôn đúng sự thật", "Có bản quyền bảo hộ"], "answer": "Tuyệt đối an toàn và luôn đúng sự thật", "explanation": "Thông tin trên mạng rất đa dạng, có cả tin giả và kém chất lượng."},
        {"id": 1202, "level": "Dễ", "type": "đúng sai", "question": "Thông tin từ trang web chính phủ (.gov.vn) thường có độ tin cậy cao hơn blog cá nhân.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Cơ quan chính phủ chịu trách nhiệm pháp lý về nguồn thông tin cung cấp."},
        {"id": 1203, "level": "Trung bình", "type": "trắc nghiệm", "question": "Khi tìm kiếm thông tin trên Internet, việc kiểm chứng tác giả và nguồn gốc giúp ích gì?", "options": ["Tăng độ tin cậy của thông tin", "Làm máy tính chạy nhanh hơn", "Giảm dung lượng tệp", "Tăng tốc độ mạng"], "answer": "Tăng độ tin cậy của thông tin", "explanation": "Xác định rõ nguồn giúp tránh sử dụng thông tin sai lệch."},
        {"id": 1204, "level": "Trung bình", "type": "trả lời ngắn", "question": "Kỹ thuật tìm kiếm thông tin trên Google bằng cách đặt từ khóa trong dấu gì để tìm chính xác cụm từ?", "answer": "ngoặc kép", "explanation": "Dùng dấu ngoặc kép \"...\" để tìm kiếm chính xác cụm từ khóa."},
        {"id": 1205, "level": "Dễ", "type": "trắc nghiệm", "question": "Hành vi chia sẻ thông tin chưa kiểm chứng lên mạng xã hội có thể gây ra điều gì?", "options": ["Lan truyền tin giả và gây hoang mang", "Giúp ích cho cộng đồng", "Được thưởng điểm", "Tăng bảo mật"], "answer": "Lan truyền tin giả và gây hoang mang", "explanation": "Cần có tư duy phản biện trước khi chia sẻ thông tin trực tuyến."},
        {"id": 1206, "level": "Dễ", "type": "đúng sai", "question": "Thư điện tử (Email) cho phép đính kèm tệp tài liệu, hình ảnh để trao đổi thông tin nhanh chóng.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Email là công cụ trao đổi thông tin chính thống và phổ biến trong học tập, công việc."},
        {"id": 1207, "level": "Trung bình", "type": "trắc nghiệm", "question": "Điện toán đám mây cho phép người dùng lưu trữ dữ liệu ở đâu?", "options": ["Trên các máy chủ kết nối Internet (đám mây)", "Chỉ trong ổ cứng USB", "Trong bộ nhớ tạm RAM", "Trong khay đĩa CD"], "answer": "Trên các máy chủ kết nối Internet (đám mây)", "explanation": "Dữ liệu lưu trên đám mây giúp dễ dàng chia sẻ và đồng bộ."},
        {"id": 1208, "level": "Dễ", "type": "trắc nghiệm", "question": "Đâu là dịch vụ lưu trữ đám mây phổ biến hiện nay?", "options": ["Google Drive, OneDrive", "Microsoft Word", "Python IDLE", "GIMP"], "answer": "Google Drive, OneDrive", "explanation": "Google Drive và OneDrive là các dịch vụ lưu trữ đám mây quen thuộc."},
        {"id": 1209, "level": "Trung bình", "type": "trắc nghiệm", "question": "Khi tìm kiếm hình ảnh trên Google, ta có thể dùng công cụ nào để tìm ảnh gốc hoặc ảnh tương tự?", "options": ["Tìm kiếm bằng hình ảnh (Google Lens)", "Tắt máy tính", "Đổi tên tệp", "Xóa bộ nhớ đệm"], "answer": "Tìm kiếm bằng hình ảnh (Google Lens)", "explanation": "Google Lens hỗ trợ nhận diện và truy xuất nguồn gốc hình ảnh."},
        {"id": 1210, "level": "Dễ", "type": "đúng sai", "question": "Mỗi thư mục trên máy tính có thể chứa cả tệp tin và các thư mục con khác.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Cấu trúc cây thư mục giúp quản lý dữ liệu ngăn nắp, khoa học."},
        {"id": 1211, "level": "Trung bình", "type": "trắc nghiệm", "question": "Quy tắc an toàn khi giao tiếp qua mạng là gì?", "options": ["Không tiết lộ thông tin cá nhân và tôn trọng người khác", "Nói xấu bạn bè thỏa thích", "Dùng mật khẩu là 123456", "Kết bạn với mọi người lạ"], "answer": "Không tiết lộ thông tin cá nhân và tôn trọng người khác", "explanation": "Bảo vệ thông tin cá nhân là kỹ năng sống còn trên không gian mạng."},
        {"id": 1212, "level": "Dễ", "type": "trắc nghiệm", "question": "Thao tác nào giúp bảo vệ tài khoản trực tuyến của bạn tốt nhất?", "options": ["Sử dụng mật khẩu mạnh và xác thực 2 bước", "Dùng chung mật khẩu cho mọi tài khoản", "Lưu mật khẩu ra giấy dán màn hình", "Không bao giờ đổi mật khẩu"], "answer": "Sử dụng mật khẩu mạnh và xác thực 2 bước", "explanation": "Xác thực 2 bước (2FA) giúp ngăn chặn kẻ gian xâm nhập tài khoản."},
        {"id": 1213, "level": "Trung bình", "type": "trắc nghiệm", "question": "Mã độc (Malware) bao gồm các loại phần mềm nào?", "options": ["Virus, Trojan, Worm, Ransomware", "Word, Excel, PowerPoint", "GIMP, Scratch", "Windows, Linux"], "answer": "Virus, Trojan, Worm, Ransomware", "explanation": "Đây là các phần mềm độc hại nguy hiểm đối với hệ thống máy tính."},
        {"id": 1214, "level": "Dễ", "type": "đúng sai", "question": "Phần mềm diệt virus giúp phát hiện và ngăn chặn kịp thời các mã độc tấn công máy tính.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Cần cài đặt và cập nhật phần mềm diệt virus thường xuyên."},
        {"id": 1215, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thế nào là hành vi bắt nạt trên không gian mạng (Cyberbullying)?", "options": ["Dùng mạng xã hội lăng mạ, đe dọa hoặc bôi nhọ người khác", "Nhắn tin chúc ngủ ngon cho bạn bè", "Đăng ảnh phong cảnh đẹp", "Chơi game trực tuyến cùng đội nhóm"], "answer": "Dùng mạng xã hội lăng mạ, đe dọa hoặc bôi nhọ người khác", "explanation": "Bắt nạt qua mạng gây tổn thương tâm lý nghiêm trọng cho học sinh."},
        {"id": 1216, "level": "Dễ", "type": "trắc nghiệm", "question": "Khi nhận được một email lạ có đính kèm đường liên kết đáng ngờ, bạn nên làm gì?", "options": ["Không bấm vào liên kết và báo cáo spam", "Bấm ngay để xem có quà gì không", "Chuyển tiếp cho toàn trường", "Tải xuống mở tệp ngay"], "answer": "Không bấm vào liên kết và báo cáo spam", "explanation": "Tránh sập bẫy lừa đảo trực tuyến (Phishing)."},
        {"id": 1217, "level": "Trung bình", "type": "trắc nghiệm", "question": "Đâu là khái niệm chỉ quyền hợp pháp của tác giả đối với sản phẩm sáng tạo của mình?", "options": ["Quyền tác giả (Copyright)", "Quyền sở hữu công cộng", "Quyền tự do chia sẻ", "Mã nguồn mở"], "answer": "Quyền tác giả (Copyright)", "explanation": "Pháp luật bảo hộ quyền tác giả đối với các sản phẩm văn hóa, thông tin."},
        {"id": 1218, "level": "Dễ", "type": "đúng sai", "question": "Việc sao chép bài viết của người khác rồi nhận là của mình trong bài thu hoạch là vi phạm đạo đức.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Đạo văn là hành vi thiếu trung thực trong học tập và nghiên cứu."},
        {"id": 1219, "level": "Trung bình", "type": "trắc nghiệm", "question": "Lợi ích của việc sử dụng phần mềm bản quyền là gì?", "options": ["Được hỗ trợ kỹ thuật, cập nhật vá lỗi và an toàn", "Bị nhiễm mã độc nhiều hơn", "Không bao giờ dùng được", "Vi phạm pháp luật"], "answer": "Được hỗ trợ kỹ thuật, cập nhật vá lỗi và an toàn", "explanation": "Sử dụng phần mềm bản quyền giúp bảo vệ thiết bị khỏi rủi ro bảo mật."},
        {"id": 1220, "level": "Dễ", "type": "trắc nghiệm", "question": "Công cụ nào giúp tìm kiếm nhanh các tập tin trên hệ điều hành Windows?", "options": ["Thanh tìm kiếm (Search) trong File Explorer", "Bàn phím", "Màn hình nền", "Chuột máy tính"], "answer": "Thanh tìm kiếm (Search) trong File Explorer", "explanation": "File Explorer cung cấp ô tìm kiếm giúp định vị nhanh chóng tệp tin."}
    ],
    "Chủ đề 3: Đạo đức, pháp luật và văn hoá trong môi trường số": [
        {"id": 1301, "level": "Dễ", "type": "trắc nghiệm", "question": "Hành vi nào vi phạm pháp luật khi sử dụng môi trường số?", "options": ["Phát tán video bạo lực học đường lên mạng", "Học lập trình Python trực tuyến", "Gửi email chúc mừng sinh nhật", "Tìm kiếm tài liệu học tập"], "answer": "Phát tán video bạo lực học đường lên mạng", "explanation": "Phát tán cảnh bạo lực vi phạm nghiêm trọng pháp luật và đạo đức."},
        {"id": 1302, "level": "Dễ", "type": "đúng sai", "question": "Sử dụng hình ảnh cá nhân của người khác để chế ảnh bêu rếu trên mạng là hành vi vi phạm pháp luật.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Quyền về hình ảnh cá nhân được pháp luật dân sự bảo vệ."},
        {"id": 1303, "level": "Trung bình", "type": "trắc nghiệm", "question": "Hành vi nào thể hiện văn hóa ứng xử tốt trên mạng xã hội?", "options": ["Biết ơn, lịch sự, tôn trọng người khác khi bình luận", "Dùng lời lẽ khiếm nhã khi không cùng quan điểm", "Chửi bới ẩn danh", "Chia sẻ tin tức giật gân sai sự thật"], "answer": "Biết ơn, lịch sự, tôn trọng người khác khi bình luận", "explanation": "Văn hóa mạng bắt nguồn từ sự tôn trọng lẫn nhau."},
        {"id": 1304, "level": "Trung bình", "type": "trả lời ngắn", "question": "Luật An ninh mạng của Việt Nam được Quốc hội thông qua vào năm nào? (Nhập 4 chữ số)", "answer": "2018", "explanation": "Luật An ninh mạng số 24/2018/QH14 được thông qua năm 2018."},
        {"id": 1305, "level": "Dễ", "type": "trắc nghiệm", "question": "Đâu là biểu hiện của việc vi phạm bản quyền số?", "options": ["Tải và bán lại phần mềm có bản quyền khi chưa được phép", "Tự viết mã nguồn chương trình của mình", "Sử dụng phần mềm miễn phí mã nguồn mở", "Đọc sách điện tử được nhà trường cấp phép"], "answer": "Tải và bán lại phần mềm có bản quyền khi chưa được phép", "explanation": "Kinh doanh trái phép phần mềm bản quyền là hành vi vi phạm pháp luật."},
        {"id": 1306, "level": "Dễ", "type": "đúng sai", "question": "Thông tin cá nhân như số căn cước, số điện thoại, địa chỉ nhà cần được giữ bí mật trên mạng.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Bảo vệ thông tin định danh cá nhân giúp tránh bị kẻ xấu lợi dụng lừa đảo."},
        {"id": 1307, "level": "Trung bình", "type": "trắc nghiệm", "question": "Khi phát hiện bạn bè bị bắt nạt trên không gian mạng, em nên làm gì?", "options": ["Báo cáo cho người lớn, thầy cô hoặc cơ quan chức năng", "Hùa theo vào bình luận chê bai", "Xem như không thấy", "Chụp lại gửi rộng rãi hơn"], "answer": "Báo cáo cho người lớn, thầy cô hoặc cơ quan chức năng", "explanation": "Cần can thiệp tích cực hoặc báo cáo để bảo vệ nạn nhân."},
        {"id": 1308, "level": "Dễ", "type": "trắc nghiệm", "question": "Hành vi tung tin đồn thất thiệt trên mạng xã hội nhằm hạ uy tín người khác sẽ bị xử lý thế nào?", "options": ["Có thể bị xử phạt vi phạm hành chính hoặc truy cứu trách nhiệm hình sự", "Không bị xử lý gì cả", "Chỉ bị nhắc nhở", "Được thưởng"], "answer": "Có thể bị xử phạt vi phạm hành chính hoặc truy cứu trách nhiệm hình sự", "explanation": "Pháp luật có chế tài nghiêm khắc đối với việc tung tin giả gây hậu quả."},
        {"id": 1309, "level": "Trung bình", "type": "trắc nghiệm", "question": "Ý nghĩa của việc tuân thủ pháp luật trong môi trường số là gì?", "options": ["Xây dựng không gian mạng lành mạnh, an toàn và văn minh", "Làm cho mạng chậm đi", "Hạn chế quyền tự do ngôn luận chính đáng", "Không có ý nghĩa gì"], "answer": "Xây dựng không gian mạng lành mạnh, an toàn và văn minh", "explanation": "Môi trường mạng văn minh bảo vệ quyền lợi của tất cả công dân."},
        {"id": 1310, "level": "Dễ", "type": "đúng sai", "question": "Nghiêm cấm lợi dụng không gian mạng để thực hiện hành vi lừa đảo chiếm đoạt tài sản.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Đây là hành vi vi phạm pháp luật nghiêm trọng được quy định trong Luật An ninh mạng."},
        {"id": 1311, "level": "Trung bình", "type": "trắc nghiệm", "question": "Khi trích dẫn tài liệu từ Internet vào bài báo cáo của mình, em cần làm gì?", "options": ["Ghi rõ nguồn gốc và tên tác giả", "Nhận là do mình tự nghĩ ra hoàn toàn", "Xóa tên tác giả gốc", "Cắt xén nội dung tùy ý"], "answer": "Ghi rõ nguồn gốc và tên tác giả", "explanation": "Trích dẫn chuẩn xác thể hiện sự tôn trọng quyền tác giả và văn hóa học tập."},
        {"id": 1312, "level": "Dễ", "type": "trắc nghiệm", "question": "Tác hại của việc nghiện trò chơi điện tử trực tuyến quá mức là gì?", "options": ["Ảnh hưởng sức khỏe, kết quả học tập sụt giảm và mất thời gian", "Giúp phát triển trí tuệ siêu việt", "Không có tác hại gì", "Làm mắt tinh hơn"], "answer": "Ảnh hưởng sức khỏe, kết quả học tập sụt giảm và mất thời gian", "explanation": "Cần cân bằng hợp lý giữa học tập, giải trí và thời gian sử dụng thiết bị."},
        {"id": 1313, "level": "Trung bình", "type": "trắc nghiệm", "question": "Hành vi truy cập trái phép vào mật khẩu hoặc hộp thư điện tử của người khác bị coi là gì?", "options": ["Xâm phạm quyền riêng tư và vi phạm pháp luật", "Hành động bình thường", "Khám phá thú vị", "Giúp đỡ bạn bè"], "answer": "Xâm phạm quyền riêng tư và vi phạm pháp luật", "explanation": "Thư tín và tài khoản cá nhân được pháp luật bảo vệ tuyệt đối."},
        {"id": 1314, "level": "Dễ", "type": "đúng sai", "question": "Ứng xử có văn hóa trên mạng nghĩa là dùng lời lẽ lịch sự, tôn trọng ngay cả khi tranh luận khác ý kiến.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Văn hóa ứng xử số phản ánh phẩm chất đạo đức của mỗi cá nhân."},
        {"id": 1315, "level": "Trung bình", "type": "trắc nghiệm", "question": "Đâu là biện pháp phòng tránh lừa đảo trực tuyến hiệu quả nhất cho học sinh?", "options": ["Nâng cao cảnh giác, không cung cấp OTP và thông tin cá nhân cho người lạ", "Tin tưởng mọi lời hứa hẹn trúng thưởng", "Chuyển tiền khi có người yêu cầu qua mạng", "Kết bạn với mọi tài khoản ảo"], "answer": "Nâng cao cảnh giác, không cung cấp OTP và thông tin cá nhân cho người lạ", "explanation": "Kẻ lừa đảo thường lợi dụng lòng tin để chiếm đoạt tài sản."},
        {"id": 1316, "level": "Dễ", "type": "trắc nghiệm", "question": "Việc tự ý cài đặt phần mềm bẻ khóa (crack) có nguy cơ gì đối với máy tính?", "options": ["Nhiễm mã độc, virus và bị đánh cắp dữ liệu", "Máy chạy nhanh hơn", "Được nhà sản xuất hỗ trợ", "An toàn tuyệt đối"], "answer": "Nhiễm mã độc, virus và bị đánh cắp dữ liệu", "explanation": "Phần mềm crack thường ẩn chứa mã độc hại nguy hiểm."},
        {"id": 1317, "level": "Trung bình", "type": "trắc nghiệm", "question": "Theo Luật Sở hữu trí tuệ, hành vi nào dưới đây được phép nếu không vì mục đích thương mại?", "options": ["Trích dẫn hợp lý để minh họa trong bài học, có ghi nguồn", "Sao chép toàn bộ một cuốn sách bán ra thị trường", "Phát tán phim chiếu rạp mới nhất", "Sao chép phần mềm thương mại"], "answer": "Trích dẫn hợp lý để minh họa trong bài học, có ghi nguồn", "explanation": "Pháp luật cho phép trích dẫn hợp lý phục vụ học tập, giảng dạy có ghi nguồn."},
        {"id": 1318, "level": "Dễ", "type": "đúng sai", "question": "Mọi thông tin xuất hiện trên mạng xã hội đều đã được cơ quan chức năng kiểm duyệt.", "options": ["Đúng", "Sai"], "answer": "Sai", "explanation": "Mạng xã hội có lượng thông tin khổng lồ chưa được kiểm chứng, người dùng phải có tư duy chọn lọc."},
        {"id": 1319, "level": "Trung bình", "type": "trắc nghiệm", "question": "Hành vi nào sau đây thể hiện tinh thần công dân số có trách nhiệm?", "options": ["Tuyên truyền thông tin tích cực, đấu tranh với tin giả", "A dua theo đám đông chửi bới người khác", "Tạo tài khoản ảo để nói xấu", "Xả rác thiết bị điện tử bừa bãi"], "answer": "Tuyên truyền thông tin tích cực, đấu tranh với tin giả", "explanation": "Công dân số trách nhiệm đóng góp xây dựng môi trường mạng lành mạnh."},
        {"id": 1320, "level": "Dễ", "type": "trắc nghiệm", "question": "Cơ quan nào ở Việt Nam tiếp nhận các tố giác, tin báo về tội phạm mạng?", "options": ["Cơ quan Công an (Công an mạng / An ninh mạng)", "Cửa hàng bán điện thoại", "Nhà mạng viễn thông", "Công ty sản xuất phần mềm"], "answer": "Cơ quan Công an (Công an mạng / An ninh mạng)", "explanation": "Lực lượng Công an chịu trách nhiệm xử lý các hành vi phạm pháp trên không gian mạng."}
    ],
    "Chủ đề 4: Ứng dụng tin học": [
        {"id": 1401, "level": "Dễ", "type": "trắc nghiệm", "question": "Trong chương trình bảng tính Excel, địa chỉ nào sau đây là địa chỉ tuyệt đối?", "options": ["C4", "$C$4", "C$4", "$C4"], "answer": "$C$4", "explanation": "Địa chỉ tuyệt đối có ký hiệu dấu $ cố định cả cột và hàng."},
        {"id": 1402, "level": "Dễ", "type": "đúng sai", "question": "Khi sao chép công thức chứa địa chỉ tuyệt đối, các thành phần có gắn dấu $ sẽ không thay đổi.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Địa chỉ tuyệt đối giữ nguyên vị trí ô khi sao chép công thức."},
        {"id": 1403, "level": "Trung bình", "type": "trắc nghiệm", "question": "Phím tắt nào giúp nhanh chóng chuyển đổi kiểu địa chỉ ô khi nhập công thức?", "options": ["F4", "F2", "F1", "F12"], "answer": "F4", "explanation": "Nhấn phím F4 để chuyển đổi linh hoạt các dạng địa chỉ ô."},
        {"id": 1404, "level": "Trung bình", "type": "trả lời ngắn", "question": "Trong Excel, hàm nào dùng để tính trung bình cộng của một dãy số? (Nhập tên hàm viết hoa)", "answer": "AVERAGE", "explanation": "Hàm AVERAGE thực hiện tính trung bình cộng các số."},
        {"id": 1405, "level": "Dễ", "type": "trắc nghiệm", "question": "Loại biểu đồ nào thích hợp nhất để so sánh các phần với tổng thể?", "options": ["Biểu đồ hình quạt tròn (Pie Chart)", "Biểu đồ đoạn thẳng", "Biểu đồ cột chồng", "Biểu đồ phân tán"], "answer": "Biểu đồ hình quạt tròn (Pie Chart)", "explanation": "Biểu đồ tròn thể hiện rất rõ tỉ lệ phần trăm các phần so với tổng thể."},
        {"id": 1406, "level": "Dễ", "type": "đúng sai", "question": "Biểu đồ cột (Column Chart) rất thích hợp để so sánh dữ liệu giữa các nhóm khác nhau.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Biểu đồ cột trực quan hóa việc so sánh các giá trị dữ liệu."},
        {"id": 1407, "level": "Trung bình", "type": "trắc nghiệm", "question": "Hàm COUNT trong Excel dùng để làm gì?", "options": ["Đếm số lượng các ô chứa dữ liệu số", "Tính tổng các số", "Tìm giá trị lớn nhất", "Tính trung bình"], "answer": "Đếm số lượng các ô chứa dữ liệu số", "explanation": "Hàm COUNT chỉ đếm các ô có giá trị số trong vùng chọn."},
        {"id": 1408, "level": "Dễ", "type": "trắc nghiệm", "question": "Phần mềm GIMP là ứng dụng dùng để làm gì?", "options": ["Chỉnh sửa và xử lý ảnh đồ họa", "Soạn thảo văn bản", "Lập trình robot", "Tính toán bảng tính"], "answer": "Chỉnh sửa và xử lý ảnh đồ họa", "explanation": "GIMP là phần mềm nguồn mở mạnh mẽ chuyên dùng cho xử lý ảnh số."},
        {"id": 1409, "level": "Trung bình", "type": "trắc nghiệm", "question": "Trong phần mềm GIMP, công cụ Crop dùng để làm gì?", "options": ["Cắt bỏ các phần ảnh không cần thiết để tạo bố cục", "Tô màu nền", "Viết chữ nghệ thuật", "Tạo hiệu ứng mờ"], "answer": "Cắt bỏ các phần ảnh không cần thiết để tạo bố cục", "explanation": "Crop giúp cô đọng khung hình và cắt bỏ chi tiết thừa."},
        {"id": 1410, "level": "Dễ", "type": "đúng sai", "question": "Các lớp ảnh (Layers) trong GIMP giúp chỉnh sửa từng thành phần của bức ảnh độc lập với nhau.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Hệ thống lớp (Layer) là cốt lõi trong chỉnh sửa ảnh chuyên nghiệp."},
        {"id": 1411, "level": "Trung bình", "type": "trắc nghiệm", "question": "Hàm IF trong Excel thực hiện chức năng gì?", "options": ["Kiểm tra điều kiện và trả về giá trị tương ứng tùy theo đúng hay sai", "Tính tổng tự động", "Sắp xếp dữ liệu", "Lọc dữ liệu"], "answer": "Kiểm tra điều kiện và trả về giá trị tương ứng tùy theo đúng hay sai", "explanation": "Hàm điều kiện IF giúp thực hiện các bài toán logic trong bảng tính."},
        {"id": 1412, "level": "Dễ", "type": "trắc nghiệm", "question": "Kết quả của hàm `=MAX(5, 10, 2, 8)` trong Excel là bao nhiêu?", "options": ["10", "5", "8", "2"], "answer": "10", "explanation": "Hàm MAX tìm giá trị lớn nhất trong danh sách các số."},
        {"id": 1413, "level": "Trung bình", "type": "trắc nghiệm", "question": "Để sắp xếp dữ liệu trong một cột theo thứ tự giảm dần, ta sử dụng tùy chọn nào trong Excel?", "options": ["Z to A (Descending)", "A to Z (Ascending)", "Filter", "Merge"], "answer": "Z to A (Descending)", "explanation": "Z to A sắp xếp dữ liệu từ lớn đến bé hoặc từ chữ Z về A."},
        {"id": 1414, "level": "Dễ", "type": "đúng sai", "question": "Chức năng Lọc (Filter) giúp ẩn đi các dòng không thỏa mãn điều kiện và chỉ hiển thị dữ liệu cần xem.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Bộ lọc Filter hỗ trợ phân tích dữ liệu nhanh chóng."},
        {"id": 1415, "level": "Trung bình", "type": "trắc nghiệm", "question": "Trong phần mềm GIMP, định dạng tệp mặc định để lưu dự án có các lớp ảnh là gì?", "options": [".xcf", ".jpg", ".png", ".mp4"], "answer": ".xcf", "explanation": ".xcf là định dạng lưu trữ toàn bộ các lớp và thuộc tính chỉnh sửa của GIMP."},
        {"id": 1416, "level": "Dễ", "type": "trắc nghiệm", "question": "Định dạng ảnh nào sau đây hỗ trợ nền trong suốt (Transparency)?", "options": ["PNG", "JPG", "BMP", "GIF động"], "answer": "PNG", "explanation": "Định dạng PNG hỗ trợ lưu ảnh có vùng trong suốt tối ưu."},
        {"id": 1417, "level": "Trung bình", "type": "trắc nghiệm", "question": "Hàm nào trong Excel dùng để đếm số lượng ô thỏa mãn một điều kiện cho trước?", "options": ["COUNTIF", "SUM", "AVERAGE", "COUNTA"], "answer": "COUNTIF", "explanation": "COUNTIF kết hợp giữa đếm số và điều kiện lọc logic."},
        {"id": 1418, "level": "Dễ", "type": "đúng sai", "question": "Biểu đồ đoạn thẳng (Line Chart) thích hợp để biểu diễn sự thay đổi của dữ liệu theo thời gian.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Biểu đồ đường thể hiện xu hướng tăng giảm theo thời gian rất tốt."},
        {"id": 1419, "level": "Trung bình", "type": "trắc nghiệm", "question": "Công cụ nào trong GIMP giúp tẩy xóa một chi tiết thừa trên ảnh bằng cách lấy mẫu từ vùng khác?", "options": ["Clone Tool (Công cụ nhân bản)", "Eraser", "Brush", "Bucket Fill"], "answer": "Clone Tool (Công cụ nhân bản)", "explanation": "Clone Tool sao chép pixel từ vùng mẫu để che phủ chi tiết không muốn."},
        {"id": 1420, "level": "Dễ", "type": "trắc nghiệm", "question": "Thao tác gộp nhiều ô thành một ô và căn giữa nội dung trong Excel sử dụng nút lệnh nào?", "options": ["Merge & Center", "Wrap Text", "Format Painter", "Sort"], "answer": "Merge & Center", "explanation": "Merge & Center gộp ô và căn giữa chữ tự động."}
    ],
    "Chủ đề 5: Giải quyết vấn đề với sự trợ giúp của máy tính (Scratch)": [
        {"id": 1501, "level": "Dễ", "type": "trắc nghiệm", "question": "Trong ngôn ngữ Scratch, khối lệnh 'lặp lại đến khi <điều kiện>' thuộc cấu trúc nào?", "options": ["Cấu trúc lặp có điều kiện kết thúc", "Cấu trúc tuần tự", "Cấu trúc rẽ nhánh", "Cấu trúc lặp số lần định trước"], "answer": "Cấu trúc lặp có điều kiện kết thúc", "explanation": "Lệnh lặp kiểm tra điều kiện để dừng vòng lặp."},
        {"id": 1502, "level": "Dễ", "type": "đúng sai", "question": "Cấu trúc rẽ nhánh trong Scratch được thể hiện qua khối lệnh 'nếu <điều kiện> thì... còn không thì...'.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Khối lệnh điều kiện if-else thực hiện rẽ nhánh tùy thuộc biểu thức logic."},
        {"id": 1503, "level": "Trung bình", "type": "trắc nghiệm", "question": "Có mấy loại lỗi chính khi lập trình và kiểm thử chương trình?", "options": ["2 loại (Lỗi cú pháp và lỗi lôgic)", "1 loại", "3 loại", "4 loại"], "answer": "2 loại (Lỗi cú pháp và lỗi lôgic)", "explanation": "Lỗi cú pháp do sai quy tắc, lỗi lôgic do sai hướng giải quyết thuật toán."},
        {"id": 1504, "level": "Trung bình", "type": "trả lời ngắn", "question": "Trong Scratch, khối lệnh có hình lục giác chứa các phép toán so sánh (> , < , =) thường dùng cho biểu thức gì?", "answer": "điều kiện", "explanation": "Khối lệnh trả về giá trị Đúng/Sai dùng cho điều kiện rẽ nhánh hoặc vòng lặp."},
        {"id": 1505, "level": "Dễ", "type": "trắc nghiệm", "question": "Để nhân vật di chuyển 10 bước trong Scratch, ta dùng khối lệnh nào?", "options": ["di chuyển 10 bước", "nói Xin chào", "đặt kích thước", "quay 15 độ"], "answer": "di chuyển 10 bước", "explanation": "Khối lệnh chuyển động trong nhóm Motion."},
        {"id": 1506, "level": "Dễ", "type": "đúng sai", "question": "Biến (Variable) trong Scratch dùng để lưu trữ dữ liệu trong quá trình thực hiện chương trình.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Biến giúp lưu điểm số, tên người chơi hoặc trạng thái tính toán."},
        {"id": 1507, "level": "Trung bình", "type": "trắc nghiệm", "question": "Khối lệnh nào trong Scratch dùng để lặp lại một công việc với số lần xác định trước?", "options": ["lặp lại <10> lần", "liên tục", "đợi 1 giây", "nếu... thì"], "answer": "lặp lại <10> lần", "explanation": "Vòng lặp hữu hạn số lần lặp định trước."},
        {"id": 1508, "level": "Dễ", "type": "trắc nghiệm", "question": "Để chương trình Scratch bắt đầu chạy khi người dùng bấm vào lá cờ xanh, ta dùng sự kiện nào?", "options": ["khi bấm vào lá cờ xanh", "khi bấm phím cách", "khi bấm nhân vật", "khi nhận tin nhắn"], "answer": "khi bấm vào lá cờ xanh", "explanation": "Sự kiện lá cờ xanh là điểm khởi đầu phổ biến nhất trong Scratch."},
        {"id": 1509, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thế nào là lỗi cú pháp trong lập trình?", "options": ["Viết sai quy tắc ngữ pháp của ngôn ngữ lập trình", "Chương trình chạy ra kết quả sai lệch", "Chương trình chạy quá lâu", "Máy tính bị mất điện"], "answer": "Viết sai quy tắc ngữ pháp của ngôn ngữ lập trình", "explanation": "Lỗi cú pháp dễ dàng được phần mềm phát hiện và thông báo ngay lập tức."},
        {"id": 1510, "level": "Dễ", "type": "đúng sai", "question": "Lỗi lôgic là loại lỗi chương trình vẫn chạy được nhưng cho kết quả không đúng như mong đợi.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Lỗi lôgic khó phát hiện hơn vì không báo đỏ cú pháp mà sai ở thuật toán."},
        {"id": 1511, "level": "Trung bình", "type": "trắc nghiệm", "question": "Trong Scratch, để tạo một danh sách (List) lưu trữ nhiều phần tử, ta vào nhóm lệnh nào?", "options": ["Các biến của tôi (Variables)", "Hiển thị (Looks)", "Âm thanh (Sound)", "Cảm biến (Sensing)"], "answer": "Các biến của tôi (Variables)", "explanation": "Nhóm Variables hỗ trợ tạo cả Biến đơn và Danh sách (List / Mảng)."},
        {"id": 1512, "level": "Dễ", "type": "trắc nghiệm", "question": "Khối lệnh nào trong nhóm Sensing dùng để kiểm tra xem nhân vật có chạm vào cạnh sân khấu hay không?", "options": ["đang chạm cạnh?", "phím khoảng trắng được bấm?", "màu đang chạm?", "khoảng cách đến?"], "answer": "đang chạm cạnh?", "explanation": "Khối cảm biến vị trí giúp xử lý va chạm trong trò chơi."},
        {"id": 1513, "level": "Trung bình", "type": "trắc nghiệm", "question": "Để nhân vật phát ra âm thanh tiếng mèo kêu trong Scratch, ta chọn nhóm lệnh nào?", "options": ["Âm thanh (Sound)", "Chuyển động (Motion)", "Sự kiện (Events)", "Điều khiển (Control)"], "answer": "Âm thanh (Sound)", "explanation": "Nhóm Sound quản lý phát âm thanh, nhạc cụ và hiệu ứng tiếng động."},
        {"id": 1514, "level": "Dễ", "type": "đúng sai", "question": "Nhân vật (Sprite) trong Scratch có thể đổi trang phục (Costumes) để tạo hiệu ứng chuyển động sinh động.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Thay đổi trang phục giúp nhân vật chạy, nhảy hoặc đổi biểu cảm."},
        {"id": 1515, "level": "Trung bình", "type": "trắc nghiệm", "question": "Thuật toán tìm kiếm tuần tự (Sequential Search) hoạt động như thế nào?", "options": ["Kiểm tra lần lượt từng phần tử từ đầu đến cuối danh sách", "Chia đôi danh sách liên tục", "Sắp xếp ngẫu nhiên", "Chọn ngay phần tử ở giữa"], "answer": "Kiểm tra lần lượt từng phần tử từ đầu đến cuối danh sách", "explanation": "Tìm kiếm tuần tự duyệt qua từng phần tử cho đến khi tìm thấy hoặc hết danh sách."},
        {"id": 1516, "level": "Dễ", "type": "trắc nghiệm", "question": "Sân khấu (Stage) trong Scratch có kích thước chuẩn mặc định là bao nhiêu?", "options": ["480 pixel chiều rộng và 360 pixel chiều cao", "100x100 pixel", "1920x1080 pixel", "800x600 pixel"], "answer": "480 pixel chiều rộng và 360 pixel chiều cao", "explanation": "Tọa độ sân khấu Scratch giới hạn từ -240 đến 240 theo trục X và -180 đến 180 theo trục Y."},
        {"id": 1517, "level": "Trung bình", "type": "trắc nghiệm", "question": "Để nhân vật nói câu 'Xin chào' trong 2 giây, ta dùng khối lệnh nào?", "options": ["nói Xin chào trong 2 giây", "suy nghĩ trong 2 giây", "thêm âm thanh", "đổi phông nền"], "answer": "nói Xin chào trong 2 giây", "explanation": "Khối lệnh hiển thị lời thoại dạng bong bóng hội thoại."},
        {"id": 1518, "level": "Dễ", "type": "đúng sai", "question": "Mỗi dự án Scratch có thể có nhiều nhân vật và nhiều phông nền sân khấu khác nhau.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Scratch hỗ trợ thiết kế đa nhân vật và nhiều bối cảnh phong phú."},
        {"id": 1519, "level": "Trung bình", "type": "trắc nghiệm", "question": "Ý nghĩa của việc gỡ lỗi (Debugging) trong lập trình là gì?", "options": ["Tìm và sửa chữa các lỗi trong chương trình", "Tạo thêm nhiều lỗi mới", "Xóa toàn bộ dự án", "Tăng dung lượng tệp"], "answer": "Tìm và sửa chữa các lỗi trong chương trình", "explanation": "Debugging là kỹ năng cốt lõi giúp hoàn thiện mã nguồn chương trình."},
        {"id": 1520, "level": "Dễ", "type": "trắc nghiệm", "question": "Khối lệnh 'liên tục' (forever) trong Scratch thuộc cấu trúc điều khiển nào?", "options": ["Cấu trúc lặp vô hạn", "Cấu trúc rẽ nhánh", "Cấu trúc tuần tự", "Cấu trúc chọn lựa"], "answer": "Cấu trúc lặp vô hạn", "explanation": "Vòng lặp liên tục chạy các khối lệnh bên trong mãi mãi cho đến khi dừng chương trình."}
    ],
    "Chủ đề 6: Hướng nghiệp với Tin học": [
        {"id": 1601, "level": "Dễ", "type": "trắc nghiệm", "question": "Ai được lịch sử công nhận là lập trình viên máy tính đầu tiên trên thế giới?", "options": ["Ada Lovelace", "John Von Neumann", "Charles Babbage", "Bill Gates"], "answer": "Ada Lovelace", "explanation": "Nữ bá tước Ada Lovelace đã viết thuật toán đầu tiên cho máy tính cơ học."},
        {"id": 1602, "level": "Dễ", "type": "đúng sai", "question": "Nghề nghiệp trong lĩnh vực công nghệ thông tin luôn rộng mở và bình đẳng cho cả nam và nữ.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Ngành CNTT không phân biệt giới tính, đề cao năng lực sáng tạo."},
        {"id": 1603, "level": "Trung bình", "type": "trắc nghiệm", "question": "Nhóm nghề nào sau đây thuộc lĩnh vực Tin học / Công nghệ thông tin?", "options": ["Kỹ sư phần mềm, Chuyên gia an ninh mạng, Quản trị cơ sở dữ liệu", "Bác sĩ thú y", "Kiến trúc sư xây dựng cầu đường", "Giáo viên Ngữ văn"], "answer": "Kỹ sư phần mềm, Chuyên gia an ninh mạng, Quản trị cơ sở dữ liệu", "explanation": "Đây là các vị trí công việc chủ chốt trong ngành công nghệ thông tin."},
        {"id": 1604, "level": "Trung bình", "type": "trả lời ngắn", "question": "Nữ nhà toán học Ada Lovelace sống vào thế kỷ nào ở Anh quốc? (Nhập số La Mã hoặc số thường, ví dụ: 19)", "answer": "19", "explanation": "Ada Lovelace sinh năm 1815, thuộc thế kỷ 19."},
        {"id": 1605, "level": "Dễ", "type": "trắc nghiệm", "question": "Phẩm chất quan trọng nào cần có của một người làm nghề lập trình viên?", "options": ["Tư duy logic, cẩn thận, kiên trì và ham học hỏi", "Sợ máy tính", "Không thích làm việc nhóm", "Cẩu thả"], "answer": "Tư duy logic, cẩn thận, kiên trì và ham học hỏi", "explanation": "Lập trình đòi hỏi sự chính xác cao độ và tinh thần cập nhật công nghệ liên tục."},
        {"id": 1606, "level": "Dễ", "type": "đúng sai", "question": "Ứng dụng tin học giúp nâng cao năng suất và hiệu quả công việc trong hầu hết mọi ngành nghề hiện nay.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Tin học hóa đã có mặt trong y tế, giáo dục, kinh tế, nông nghiệp và quản lý."},
        {"id": 1607, "level": "Trung bình", "type": "trắc nghiệm", "question": "Công việc của một chuyên gia an ninh mạng là gì?", "options": ["Bảo vệ hệ thống thông tin, phòng chống tấn công mạng và mã độc", "Sửa phần cứng máy in", "Bán máy tính", "Thiết kế poster quảng cáo"], "answer": "Bảo vệ hệ thống thông tin, phòng chống tấn công mạng và mã độc", "explanation": "An ninh mạng đảm bảo an toàn dữ liệu trước các mối đe dọa trực tuyến."},
        {"id": 1608, "level": "Dễ", "type": "trắc nghiệm", "question": "Lĩnh vực Trí tuệ nhân tạo (AI) và Khoa học dữ liệu (Data Science) đang có xu hướng thế nào trong tương lai?", "options": ["Phát triển mạnh mẽ và có nhu cầu nhân lực rất cao", "Đang dần mai một", "Không quan trọng", "Bị cấm sử dụng"], "answer": "Phát triển mạnh mẽ và có nhu cầu nhân lực rất cao", "explanation": "AI và Data Science định hình xu thế công nghệ toàn cầu trong kỷ nguyên số."},
        {"id": 1609, "level": "Trung bình", "type": "trắc nghiệm", "question": "Để theo đuổi các ngành nghề liên quan đến CNTT, học sinh THCS nên rèn luyện môn học nào từ sớm?", "options": ["Tin học và Toán học", "Âm nhạc và Mỹ thuật", "Lịch sử và Địa lý", "Thể dục"], "answer": "Tin học và Toán học", "explanation": "Toán học và Tin học xây dựng nền tảng tư duy thuật toán vững chắc."},
        {"id": 1610, "level": "Dễ", "type": "đúng sai", "question": "Làm việc trong lĩnh vực CNTT thường xuyên phải đối mặt với công nghệ mới nên đòi hỏi tinh thần tự học.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Công nghệ phát triển từng ngày, tự học là kỹ năng sống còn của kỹ sư công nghệ."},
        {"id": 1611, "level": "Trung bình", "type": "trắc nghiệm", "question": "Đâu là công việc của một kỹ sư phân tích dữ liệu (Data Analyst)?", "options": ["Thu thập, xử lý và trực quan hóa dữ liệu để đưa ra quyết định kinh doanh", "Sửa ống nước", "Lái xe công nghệ", "Trồng cây xanh"], "answer": "Thu thập, xử lý và trực quan hóa dữ liệu để đưa ra quyết định kinh doanh", "explanation": "Phân tích dữ liệu biến các con số thô thành thông tin chiến lược giá trị."},
        {"id": 1612, "level": "Dễ", "type": "trắc nghiệm", "question": "Nghề thiết kế đồ họa (Graphic Designer) ứng dụng phần mềm nào để sáng tạo?", "options": ["Phần mềm chỉnh sửa ảnh, đồ họa (GIMP, Photoshop, Illustrator...)", "Phần mềm gõ văn bản thuần túy", "Phần mềm diệt virus", "Trình duyệt web"], "answer": "Phần mềm chỉnh sửa ảnh, đồ họa (GIMP, Photoshop, Illustrator...)", "explanation": "Thiết kế đồ họa mang lại các sản phẩm mỹ thuật số ấn tượng."},
        {"id": 1613, "level": "Trung bình", "type": "trắc nghiệm", "question": "Tại sao các cơ quan, doanh nghiệp hiện nay rất cần chuyên gia quản trị cơ sở dữ liệu?", "options": ["Để lưu trữ, sắp xếp và bảo mật lượng dữ liệu khổng lồ của tổ chức", "Để quét rác văn phòng", "Để pha cà phê", "Để trang trí phòng làm việc"], "answer": "Để lưu trữ, sắp xếp và bảo mật lượng dữ liệu khổng lồ của tổ chức", "explanation": "Dữ liệu là tài sản quý giá của mọi tổ chức trong thời đại số."},
        {"id": 1614, "level": "Dễ", "type": "đúng sai", "question": "Kỹ năng làm việc nhóm (Teamwork) rất quan trọng đối với các dự án phát triển phần mềm lớn.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "Phần mềm phức tạp đòi hỏi sự phối hợp của nhiều lập trình viên và chuyên gia."},
        {"id": 1615, "level": "Trung bình", "type": "trắc nghiệm", "question": "Việc ứng dụng Tin học trong nông nghiệp thông minh (Smart Agriculture) giúp đạt hiệu quả gì?", "options": ["Tự động hóa tưới tiêu, giám sát thời tiết và tối ưu hóa năng suất cây trồng", "Làm tăng ô nhiễm môi trường", "Tăng chi phí nhân công thủ công", "Giảm năng suất"], "answer": "Tự động hóa tưới tiêu, giám sát thời tiết và tối ưu hóa năng suất cây trồng", "explanation": "Công nghệ IoT và AI đang cách mạng hóa ngành nông nghiệp hiện đại."},
        {"id": 1616, "level": "Dễ", "type": "trắc nghiệm", "question": "Đâu là đặc điểm của môi trường làm việc trong ngành công nghệ số?", "options": ["Năng động, sáng tạo, có thể làm việc từ xa (Remote work)", "Gò bó ở một chỗ không đổi", "Không bao giờ dùng máy tính", "Chỉ làm việc ban đêm"], "answer": "Năng động, sáng tạo, có thể làm việc từ xa (Remote work)", "explanation": "Ngành CNTT cho phép không gian làm việc linh hoạt toàn cầu."},
        {"id": 1617, "level": "Trung bình", "type": "trắc nghiệm", "question": "Học sinh THCS có thể bắt đầu rèn luyện lập trình từ ngôn ngữ nào thân thiện nhất?", "options": ["Scratch và Python", "C++ nâng cao", "Assembly", "Machine Language"], "answer": "Scratch và Python", "explanation": "Scratch trực quan và Python gần gũi rất phù hợp cho học sinh phổ thông."},
        {"id": 1618, "level": "Dễ", "type": "đúng sai", "question": "Sự bùng nổ của trí tuệ nhân tạo (AI) tạo ra cả cơ hội nghề nghiệp mới lẫn thách thức đòi hỏi nâng cao kỹ năng.", "options": ["Đúng", "Sai"], "answer": "Đúng", "explanation": "AI thay thế các công việc lặp đi lặp lại và mở ra các vị trí sáng tạo mới."},
        {"id": 1619, "level": "Trung bình", "type": "trắc nghiệm", "question": "Mục tiêu chính của giáo dục hướng nghiệp môn Tin học ở phổ thông là gì?", "options": ["Giúp học sinh hiểu biết về các nghề nghiệp CNTT và định hướng năng lực bản thân", "Bắt buộc mọi học sinh phải trở thành kỹ sư", "Chỉ để thi cử lấy điểm", "Không có mục tiêu rõ ràng"], "answer": "Giúp học sinh hiểu biết về các nghề nghiệp CNTT và định hướng năng lực bản thân", "explanation": "Hướng nghiệp giúp học sinh chuẩn bị hành trang vững chắc cho tương lai số."},
        {"id": 1620, "level": "Dễ", "type": "trắc nghiệm", "question": "Kỹ năng ngoại ngữ (đặc biệt là tiếng Anh) có vai trò thế nào trong ngành CNTT?", "options": ["Rất quan trọng vì tài liệu kỹ thuật và ngôn ngữ lập trình chủ yếu bằng tiếng Anh", "Không có tác dụng gì", "Chỉ dùng để giải trí", "Chỉ dùng khi đi du lịch"], "answer": "Rất quan trọng vì tài liệu kỹ thuật và ngôn ngữ lập trình chủ yếu bằng tiếng Anh", "explanation": "Tiếng Anh là chìa khóa mở ra kho tàng tri thức công nghệ toàn cầu."}
    ]
}

# Khởi tạo Session State
if "test_started" not in st.session_state:
    st.session_state.test_started = False
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "start_time" not in st.session_state:
    st.session_state.start_time = None
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "shuffled_questions" not in st.session_state:
    st.session_state.shuffled_questions = {}
if "student_name" not in st.session_state:
    st.session_state.student_name = ""
if "student_class" not in st.session_state:
    st.session_state.student_class = "8A4"

# Banner AI tiêu đề
st.markdown("""
    <div class="ai-banner">
        <h2>🤖 AI-POWERED SMART QUIZ HUB</h2>
        <p style="margin: 0; color: #94a3b8;">Hệ thống Kiểm tra & Đánh giá năng lực Tin học 8 - Trường THCS Đồng Phú</p>
    </div>
""", unsafe_allow_html=True)

# GIAO DIỆN CHƯA BẮT ĐẦU HOẶC ĐÃ NỘP BÀI (MÀN HÌNH ĐĂNG NHẬP THÔNG TIN)
if not st.session_state.test_started:
    st.markdown("### 📝 Đăng nhập thông tin học sinh")
    with st.form("login_form"):
        st.markdown("<div class='user-card'>", unsafe_allow_html=True)
        name_input = st.text_input("Họ và tên học sinh:", value=st.session_state.student_name, placeholder="Ví dụ: Nguyễn Văn A")
        class_input = st.text_input("Lớp:", value=st.session_state.student_class, placeholder="Ví dụ: 8A4")
        selected_topic = st.selectbox("Chọn chủ đề kiểm tra:", ["Tất cả các chủ đề (120 câu)"] + list(MASTER_QUESTIONS.keys()))
        st.markdown("</div>", unsafe_allow_html=True)
        
        start_btn = st.form_submit_button("🚀 Bắt đầu làm bài")
        if start_btn:
            if not name_input.strip():
                st.error("Vui lòng nhập đầy đủ Họ và tên trước khi bắt đầu!")
            else:
                st.session_state.student_name = name_input.strip()
                st.session_state.student_class = class_input.strip()
                st.session_state.test_started = True
                st.session_state.submitted = False
                st.session_state.start_time = time.time()  # BẮT ĐẦU TÍNH GIỜ TỪ ĐÂY
                st.session_state.user_answers = {}
                
                # Trộn ngẫu nhiên câu hỏi và đáp án
                topic_key = selected_topic
                if selected_topic.startswith("Tất cả"):
                    all_q = []
                    for q_list in MASTER_QUESTIONS.values():
                        all_q.extend(q_list)
                    random.shuffle(all_q)
                    st.session_state.shuffled_questions[topic_key] = all_q
                else:
                    q_list = list(MASTER_QUESTIONS[selected_topic])
                    random.shuffle(q_list)
                    for q in q_list:
                        if q["type"] == "trắc nghiệm":
                            random.shuffle(q["options"])
                    st.session_state.shuffled_questions[topic_key] = q_list
                st.session_state.current_topic = topic_key
                st.rerun()

else:
    # GIAO DIỆN ĐANG LÀM BÀI VÀ ĐẾM NGƯỢC THỜI GIAN
    topic_key = st.session_state.current_topic
    current_active_questions = st.session_state.shuffled_questions.get(topic_key, [])
    
    # Tính thời gian còn lại (10 phút = 600 giây)
    TIME_LIMIT = 600
    elapsed_time = int(time.time() - st.session_state.start_time)
    remaining_time = max(0, TIME_LIMIT - elapsed_time)
    
    minutes = remaining_time // 60
    seconds = remaining_time % 60
    
    # Sidebar hiển thị thông tin học sinh và đồng hồ
    st.sidebar.markdown("### 📋 Thông tin thí sinh")
    st.sidebar.markdown(f"**Học sinh:** {st.session_state.student_name}")
    st.sidebar.markdown(f"**Lớp:** {st.session_state.student_class}")
    st.sidebar.markdown(f"**Chủ đề:** {topic_key}")
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("### ⏱️ Thời gian làm bài")
    st.sidebar.markdown(f"<h2 style='color: #0066cc; margin:0;'>{minutes:02d}:{seconds:02d}</h2>", unsafe_allow_html=True)
    st.sidebar.caption("Thời gian đang tự động đếm ngược.")
    
    if remaining_time == 0 and not st.session_state.submitted:
        st.sidebar.warning("⏰ Đã hết giờ làm bài! Hệ thống tự động nộp bài.")
        st.session_state.submitted = True
        st.rerun()

    st.info(f"📌 Đang làm bài: **{topic_key}** | Tổng số câu: **{len(current_active_questions)} câu**")

    # Form làm bài kiểm tra chính thức
    if not st.session_state.submitted:
        with st.form("exam_form"):
            for idx, q in enumerate(current_active_questions):
                st.markdown(f"### Câu {idx + 1} ({q['level']})")
                st.markdown(f"**{q['question']}**")
                
                q_key = f"q_ans_{q['id']}"
                
                if q["type"] in ["trắc nghiệm", "đúng sai"]:
                    user_choice = st.radio("Lựa chọn của em:", options=q["options"], key=q_key, index=None)
                    st.session_state.user_answers[q['id']] = user_choice
                elif q["type"] == "trả lời ngắn":
                    user_input = st.text_input("Nhập câu trả lời ngắn:", key=q_key)
                    st.session_state.user_answers[q['id']] = user_input
                    
                st.markdown("---")
                
            submit_exam = st.form_submit_button("🚀 Nộp bài kiểm tra")
            if submit_exam:
                st.session_state.submitted = True
                st.rerun()

    # KẾT QUẢ VÀ LƯU BÀI LÀM SAU KHI NỘP
    if st.session_state.submitted:
        st.markdown("---")
        st.header("📊 KẾT QUẢ KIỂM TRA ĐÁNH GIÁ NĂNG LỰC")
        
        # Hiển thị thẻ xác nhận học sinh
        st.success(f"Thí sinh: **{st.session_state.student_name}** - Lớp: **{st.session_state.student_class}** đã hoàn thành bài kiểm tra!")
        
        score = 0
        total_q = len(current_active_questions)
        result_log_text = f"BÁO CÁO KẾT QUẢ KIỂM TRA TIN HỌC 8\n"
        result_log_text += f"Họ tên học sinh: {st.session_state.student_name}\n"
        result_log_text += f"Lớp: {st.session_state.student_class}\n"
        result_log_text += f"Chủ đề: {topic_key}\n"
        result_log_text += f"Thời gian nộp: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
        result_log_text += "-"*40 + "\n\n"
        
        for idx, q in enumerate(current_active_questions):
            user_ans = st.session_state.user_answers.get(q['id'])
            correct_ans = q['answer']
            
            is_correct = False
            if user_ans is not None:
                if q["type"] == "trả lời ngắn":
                    if str(user_ans).strip().lower() == str(correct_ans).strip().lower():
                        is_correct = True
                else:
                    if str(user_ans) == str(correct_ans):
                        is_correct = True
                        
            if is_correct:
                score += 1
                
            result_log_text += f"Câu {idx + 1}: {q['question']}\n"
            result_log_text += f"- Trả lời của HS: {user_ans}\n"
            result_log_text += f"- Đáp án đúng: {correct_ans}\n"
            result_log_text += f"- Kết quả: {'ĐÚNG' if is_correct else 'SAI'}\n\n"
            
            with st.container():
                if is_correct:
                    st.success(f"**Câu {idx + 1}: Đúng!** (Em chọn: {user_ans})")
                else:
                    st.error(f"**Câu {idx + 1}: Sai.** (Em chọn: {user_ans} | Đáp án đúng: **{correct_ans}**)")
                st.markdown(f"💡 *Giải thích:* {q['explanation']}")
                st.markdown("---")
                
        percentage = (score / total_q) * 100
        result_log_text += f"TỔNG KẾT: {score}/{total_q} câu đúng ({percentage:.1f}%)\n"
        
        st.metric(label="🏆 Điểm số tổng kết", value=f"{score}/{total_q} câu đúng ({percentage:.1f}%)")
        
        if percentage >= 80:
            st.balloons()
            st.success("🌟 Xuất sắc! Kết quả bài làm đạt loại Giỏi.")
        elif percentage >= 50:
            st.info("👍 Khá tốt! Em đã nắm vững kiến thức cơ bản.")
        else:
            st.warning("📚 Cần cố gắng ôn tập thêm nội dung sách giáo khoa nhé!")
            
        # Nút tải tệp kết quả bài làm để học sinh lưu lại hoặc nộp báo cáo
        st.download_button(
            label="📥 Tải xuống tệp kết quả bài làm (.txt)",
            data=result_log_text,
            file_name=f"Ket_Qua_TinHoc8_{st.session_state.student_name.replace(' ', '_')}.txt",
            mime="text/plain"
        )
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Làm lại bài mới"):
                st.session_state.test_started = False
                st.session_state.submitted = False
                st.session_state.user_answers = {}
                st.rerun()