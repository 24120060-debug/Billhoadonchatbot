import streamlit as st
from datetime import datetime
st.image("03144c6e4723b03d2060a173afcaee6e.jpg")
# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Trà Sữa - Tính Hóa Đơn",
    page_icon="🧋",
    layout="centered"
)

# =========================
# DỮ LIỆU MENU
# =========================
TRA_SUA = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa khoai môn": 38000,
    "Trà sữa ô long": 35000
}

TOPPING = {
    "Không topping": 0,
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000
}

SIZE = {
    "Size M": 0,
    "Size L": 5000
}

MON_THEM = {
    "Không thêm món": 0,
    "Bánh flan": 12000,
    "Bánh ngọt": 15000,
    "Khoai tây chiên": 20000,
    "Xúc xích": 15000
}

# =========================
# TIÊU ĐỀ
# =========================
st.title("🧋 QUÁN TRÀ SỮA")
st.subheader("Tính hóa đơn")

st.divider()

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =========================
# CHỌN MÓN
# =========================
st.header("🧋 Chọn món")

col1, col2 = st.columns(2)

with col1:
    loai_tra = st.selectbox(
        "Loại trà sữa",
        list(TRA_SUA.keys())
    )

    so_luong = st.number_input(
        "Số lượng",
        min_value=1,
        max_value=20,
        value=1,
        step=1
    )

    size_ly = st.selectbox(
        "Size ly",
        list(SIZE.keys())
    )

with col2:
    muc_duong = st.selectbox(
        "Mức độ đường",
        ["0% đường", "30% đường", "50% đường", "70% đường", "100% đường"]
    )

    muc_da = st.selectbox(
        "Mức độ đá",
        ["Không đá", "30% đá", "50% đá", "70% đá", "100% đá"]
    )

    topping = st.selectbox(
        "Topping",
        list(TOPPING.keys())
    )

# =========================
# MÓN THÊM
# =========================
st.header("🍰 Món ăn thêm")

them_mon = st.checkbox("Có thêm món")

mon_them = "Không thêm món"
so_luong_mon_them = 0

if them_mon:
    col3, col4 = st.columns(2)

    with col3:
        mon_them = st.selectbox(
            "Chọn món thêm",
            [x for x in MON_THEM.keys() if x != "Không thêm món"]
        )

    with col4:
        so_luong_mon_them = st.number_input(
            "Số lượng món thêm",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )

# =========================
# TÍNH TIỀN
# =========================
gia_tra = TRA_SUA[loai_tra]
gia_size = SIZE[size_ly]
gia_topping = TOPPING[topping]

tien_tra_sua = (gia_tra + gia_size + gia_topping) * so_luong

if them_mon:
    tien_mon_them = MON_THEM[mon_them] * so_luong_mon_them
else:
    tien_mon_them = 0

tong_tien = tien_tra_sua + tien_mon_them

# =========================
# NÚT TÍNH HÓA ĐƠN
# =========================
if st.button("🧾 XEM HÓA ĐƠN", use_container_width=True):

    if ten_khach.strip() == "":
        st.warning("⚠️ Vui lòng nhập tên khách hàng!")
    else:
        st.success("Đã tạo hóa đơn thành công!")

        st.divider()

        # =========================
        # HIỂN THỊ THÔNG TIN ĐÃ NHẬP
        # =========================
        st.header("📋 Thông tin đơn hàng")

        st.write(f"**Khách hàng:** {ten_khach}")
        st.write(f"**Loại trà sữa:** {loai_tra}")
        st.write(f"**Size:** {size_ly}")
        st.write(f"**Số lượng:** {so_luong} ly")
        st.write(f"**Đường:** {muc_duong}")
        st.write(f"**Đá:** {muc_da}")
        st.write(f"**Topping:** {topping}")

        if them_mon:
            st.write(
                f"**Món thêm:** {mon_them} × {so_luong_mon_them}"
            )
        else:
            st.write("**Món thêm:** Không có")

        # =========================
        # BẢNG TÍNH TIỀN
        # =========================
        st.subheader("💰 Chi tiết thanh toán")

        st.write(
            f"Trà sữa: **{tien_tra_sua:,.0f} VNĐ**"
        )

        if them_mon:
            st.write(
                f"Món thêm: **{tien_mon_them:,.0f} VNĐ**"
            )

        st.markdown(
            f"""
            <div style="
                background-color:#fff3e6;
                padding:20px;
                border-radius:12px;
                text-align:center;
                margin-top:20px;
            ">
                <h2>TỔNG THANH TOÁN</h2>
                <h1 style="color:#d63384;">
                    {tong_tien:,.0f} VNĐ
                </h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Lưu thông tin vào session
        st.session_state["hoa_don"] = {
            "ten_khach": ten_khach,
            "loai_tra": loai_tra,
            "so_luong": so_luong,
            "size": size_ly,
            "duong": muc_duong,
            "da": muc_da,
            "topping": topping,
            "mon_them": mon_them,
            "so_luong_mon_them": so_luong_mon_them,
            "tien_tra_sua": tien_tra_sua,
            "tien_mon_them": tien_mon_them,
            "tong_tien": tong_tien
        }

# =========================
# NÚT THANH TOÁN
# =========================
if "hoa_don" in st.session_state:

    st.divider()

    st.header("💳 Thanh toán")

    if st.button("💵 THANH TOÁN", use_container_width=True):

        hd = st.session_state["hoa_don"]

        st.success("✅ Thanh toán thành công!")

        # =========================
        # XUẤT HÓA ĐƠN
        # =========================
        st.divider()

        st.markdown(
            f"""
            <div style="
                border:2px solid #333;
                border-radius:15px;
                padding:25px;
                background-color:white;
            ">

            <h1 style="text-align:center;">
                🧋 QUÁN TRÀ SỮA
            </h1>

            <p style="text-align:center;">
                <b>HÓA ĐƠN THANH TOÁN</b>
            </p>

            <hr>

            <p>
                <b>Khách hàng:</b> {hd["ten_khach"]}
            </p>

            <p>
                <b>Thời gian:</b>
                {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
            </p>

            <hr>

            <p>
                <b>Trà sữa:</b> {hd["loai_tra"]}
            </p>

            <p>
                <b>Size:</b> {hd["size"]}
            </p>

            <p>
                <b>Số lượng:</b> {hd["so_luong"]} ly
            </p>

            <p>
                <b>Đường:</b> {hd["duong"]}
            </p>

            <p>
                <b>Đá:</b> {hd["da"]}
            </p>

            <p>
                <b>Topping:</b> {hd["topping"]}
            </p>

            <hr>

            <p>
                <b>Tiền trà sữa:</b>
                {hd["tien_tra_sua"]:,.0f} VNĐ
            </p>
            """,
            unsafe_allow_html=True
        )

        if hd["so_luong_mon_them"] > 0:
            st.markdown(
                f"""
                <div style="
                    border:2px solid #333;
                    border-top:0;
                    padding:0 25px 10px 25px;
                    background-color:white;
                ">
                    <p>
                        <b>Món thêm:</b>
                        {hd["mon_them"]} ×
                        {hd["so_luong_mon_them"]}
                    </p>

                    <p>
                        <b>Tiền món thêm:</b>
                        {hd["tien_mon_them"]:,.0f} VNĐ
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        st.markdown(
            f"""
            <div style="
                border:2px solid #333;
                border-top:0;
                border-radius:0 0 15px 15px;
                padding:15px 25px;
                background-color:white;
                text-align:right;
            ">

            <h2>
                TỔNG TIỀN:
                {hd["tong_tien"]:,.0f} VNĐ
            </h2>

            <p style="text-align:center;">
                Cảm ơn quý khách đã ủng hộ! ❤️
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()
