PHẦN 1: PHÂN TÍCH & ĐỀ XUẤT ĐA GIẢI PHÁP
1. Phân tích Input / Output
Input: * product_id (Path Parameter) dạng số nguyên để xác định sản phẩm cần sửa.

Request Body dưới dạng JSON gồm: code (mã), name (tên), price (giá), stock (tồn kho).
Output:

Thành công (200 OK): Trả về object chứa thông báo thành công và toàn bộ thông tin sản phẩm sau khi sửa.

Thất bại do sai định dạng (422 Unprocessable Entity): Lỗi do nhập tên rỗng, giá $\le 0$ hoặc số lượng tồn kho $< 0$.

Thất bại do Logic nghiệp vụ (400 Bad Request / 404 Not Found): * Trả về {"detail": "Product not found"} nếu ID không tồn tại.

Trả về {"detail": "Product code already exists"} nếu sửa mã sản phẩm trùng với mã của một sản phẩm khác.

2. Đề xuất 2 giải pháp kỹ thuật
Giải pháp 1 (Duyệt List): Sử dụng cấu trúc lưu trữ list ban đầu. Khi cần tìm sản phẩm theo id hoặc check trùng code, hệ thống sẽ chạy vòng lặp for từ đầu đến cuối danh sách để so sánh.
Giải pháp 2 (Dùng Dict): Chuyển đổi hoặc tổ chức lại cấu trúc dữ liệu ban đầu thành một Dictionary (Ví dụ: dùng id làm key: {1: {...}, 2: {...}}). Khi cần update, hệ thống chỉ cần gọi trực tiếp qua key mà không cần chạy vòng lặp.

| Tiêu chí | Giải pháp 1: Duyệt List | Giải pháp 2: Dùng Dict |
| :--- | :--- | :--- |
| **Tốc độ tìm kiếm** | Chậm hơn ($O(N)$), phải duyệt mảng khi danh sách lớn. | Cực nhanh ($O(1)$), tìm phát ra ngay dựa vào Key. |
| **Bộ nhớ** | Tiết kiệm, giữ nguyên mảng dữ liệu tuần tự. | Tốn bộ nhớ hơn một chút cho cấu trúc Key-Value. |
| **Dễ hiểu & bảo trì** | Rất trực quan, dễ viết, tư duy cơ bản. | Phức tạp hơn ở khâu quản lý cấu trúc Map. |
| **Bối cảnh phù hợp** | Phù hợp khi mảng nhỏ, bài tập thực hành trên lớp. | Phù hợp cho hệ thống lớn cần tối ưu hiệu năng. |

2. Kết luận lựa chọn
Chọn Giải pháp 1 (Duyệt List).

Lý do: Theo bối cảnh đề bài đưa ra, dữ liệu ban đầu bắt buộc lưu bằng list (products = [...]). Với số lượng phần tử nhỏ, việc duyệt list vẫn đảm bảo hiệu năng tối đa, code ngắn gọn, dễ hiểu và đáp ứng chính xác cấu trúc dữ liệu mẫu của giảng viên yêu cầu.