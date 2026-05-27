Câu 1
-Input: Nhận vào 1 tập dữ liệu, không bắt buộc phải sắp xếp theo thứ tự
-Output: Trả về vị trí của phần tử trong mảng nếu phần tử đó khớp với khóa key. Nếu tìm không thấy key trong mảng, thuật toán sẽ trả về kết quả "không tìm thấy"
-Thuật toán sẽ dừng lại vào 2 trường hợp sau:
1. Tìm thấy phần tử thành công
2. Duyệt hết danh sách
Câu 2
Bước    Chỉ số      Giá trị A[i]    So sánh(x = 5)     Kết luận
--------------------------------------------------------------------------------------
1       i = 0       A = 7           7 /= 5              Không khớp chỉ số i tăng lên 1
2       i = 1       A = 3           3 /= 5              Không khớp chỉ số i tăng lên 1
3       i = 2       A = 9           5 /= 5              Không khớp chỉ số i tăng lên 1
4       i = 3       A = 12          12 /= 5             Không khớp chỉ số i tăng lên 1
5       i = 4       A = 5           5 = 5               Tìm thấy dừng thuật toán
Giá trị hàm trả về: Thuật toán sẽ kết thúc ở bước 5 và trả về giá trị 4
Câu 3
a/ Tìm x = 7
-Phần tử 7 nằm ngay vị trí đầu mảng
-Thuật toán dừng ngay lập tức
b/ Tìm x = 1
-Phần tử 1 nằm ở vị trí cuối bảng
-Thuật toán lần lượt so sánh các giá trị trong mảng cho đến phần tử cuối cùng
c/ Tìm x = 100
-Vì 100 không tồn tại trong mảng, thuật toán bắt buộc phải duyệt và so sánh x với toàn bộ 7 phần tử của mảng. Sau khi kiểm tra đến phần tử cuối cùng mà vẫn không thấy, nó kết luận là "không tìm thấy"
Câu 4
-Trường hợp tốt nhất: Xảy ra khi phần tử cần tìm nằm ngay vị trí đầu tiên của mảng. Lúc này, thuật toán tìm thấy giá trị khớp ngay ở bước đầu tiên nên số phép so sánh là 1
-Trường hợp xấu nhất: Xảy ra khi phần tử cần tìm nằm ở vị trí cuối cùng hoặc hoàn toàn không có mặt trong mảng. Thuật toán bắt buộc phải duyệt và kiểm tra qua toàn bộ các phần tử cho đến khi kết thúc danh sách, do đó số phép so sánh đạt mức tối đa là n
-Trường hợp trung bình: Giả định phần tử cần tìm chắc chắn có trong mảng và xác suất nó nằm ở bất kỳ vị trí nào (từ vị trí thứ 1 đến vị trí thứ n) là ngang nhau. Khi đó, số phép so sánh trung bình sẽ là trung bình cộng của số phép so sánh tại mọi vị trí
Câu 5
-Tìm kiếm tuyến tính không bắt buộc mảng phải được sắp xếp trước vì thuật toán hoạt động bằng cách duyệt tuần tự từ phần tử đầu tiên và so sánh lần lượt cho đến khi hết danh sách, nên việc mảng có thứ tự hay không không ảnh hưởng đến logic của thuật toán
-Tìm kiếm tuyến tính: Có thể áp dụng cho tập dữ liệu bất kỳ, dù đã được sắp xếp hay chưa
-Tìm kiếm nhị phân: Bắt buộc chỉ áp dụng đối với dãy số đã có thứ tự 