import streamlit as st
from datetime import datetime

# =========================================================
# CẤU HÌNH TRANG
# =========================================================
st.set_page_config(
    page_title="Trà Sữa - Tính Hóa Đơn",
    page_icon="🧋",
    layout="centered"
)

# =========================================================
# DỮ LIỆU MENU
# =========================================================
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

# =========================================================
# DỮ LIỆU CHO CHATBOT
# Calo chỉ là mức ước tính tham khảo
# =========================================================
CALO = {
    "Trà sữa truyền thống": 300,
    "Trà sữa matcha": 280,
    "Trà sữa socola": 350,
    "Trà sữa dâu": 290,
    "Trà sữa khoai môn": 380,
    "Trà sữa ô long": 250
}

# Topping phù hợp với từng loại trà sữa
TOPPING_PHU_HOP = {
    "Trà sữa truyền thống": [
        "Trân châu đen",
        "Pudding trứng",
        "Trân châu trắng"
    ],
    "Trà sữa matcha": [
        "Trân châu trắng",
        "Pudding trứng",
        "Kem cheese"
    ],
    "Trà sữa socola": [
        "Pudding trứng",
        "Kem cheese",
        "Trân châu đen"
    ],
    "Trà sữa dâu": [
        "Thạch trái cây",
        "Trân châu trắng",
        "Kem cheese"
    ],
    "Trà sữa khoai môn": [
        "Pudding trứng",
        "Trân châu trắng",
        "Kem cheese"
    ],
    "Trà sữa ô long": [
        "Trân châu trắng",
        "Thạch trái cây",
        "Kem cheese"
    ]
}

# =========================================================
# HÀM CHATBOT RULE-BASED
# =========================================================
def chatbot_tra_sua(cau_hoi):

    q = cau_hoi.lower().strip()

    # -----------------------------------------------------
    # 1. GIÁ CAO NHẤT
    # -----------------------------------------------------
    if (
        "giá cao nhất" in q
        or "đắt nhất" in q
        or "cao nhất" in q
        or "mắc nhất" in q
    ):
        gia_max = max(TRA_SUA.values())

        mon_max = [
            ten for ten, gia in TRA_SUA.items()
            if gia == gia_max
        ]

        return (
            f"💰 Loại trà sữa có giá cao nhất là: "
            f"**{', '.join(mon_max)}** "
            f"với giá **{gia_max:,.0f} VNĐ/ly**."
        )

    # -----------------------------------------------------
    # 2. GIÁ THẤP NHẤT
    # -----------------------------------------------------
    if (
        "giá thấp nhất" in q
        or "rẻ nhất" in q
        or "thấp nhất" in q
        or "giá rẻ" in q
    ):
        gia_min = min(TRA_SUA.values())

        mon_min = [
            ten for ten, gia in TRA_SUA.items()
            if gia == gia_min
        ]

        return (
            f"💵 Loại trà sữa có giá thấp nhất là: "
            f"**{', '.join(mon_min)}** "
            f"với giá **{gia_min:,.0f} VNĐ/ly**."
        )

    # -----------------------------------------------------
    # 3. LOẠI TRÀ SỮA + TOPPING
    # -----------------------------------------------------
    for ten_tra in TRA_SUA.keys():

        tu_khoa = ten_tra.lower()

        if tu_khoa in q:

            topping_goi_y = TOPPING_PHU_HOP[ten_tra]

            return (
                f"🧋 Với **{ten_tra}**, bạn có thể chọn:\n\n"
                f"• {topping_goi_y[0]}\n"
                f"• {topping_goi_y[1]}\n"
                f"• {topping_goi_y[2]}\n\n"
                f"💡 Đây là các topping được gợi ý để kết hợp "
                f"với hương vị của loại trà sữa này."
            )

    # -----------------------------------------------------
    # 4. HỎI TOPPING PHÙ HỢP
    # -----------------------------------------------------
    if (
        "topping nào" in q
        or "topping gì" in q
        or "topping phù hợp" in q
        or "topping hợp" in q
    ):
        return (
            "🧋 Bạn hãy nhập tên loại trà sữa bạn muốn hỏi, "
            "ví dụ:\n\n"
            "👉 *Trà sữa matcha kèm topping nào?*\n\n"
            "👉 *Trà sữa socola nên ăn topping gì?*"
        )

    # -----------------------------------------------------
    # 5. TRÀ SỮA ÍT NGỌT / ÍT CALO
    # -----------------------------------------------------
    if (
        "ít ngọt" in q
        or "ít đường" in q
        or "ít calo" in q
        or "ít calories" in q
    ):
        calo_min = min(CALO.values())

        mon_it = [
            ten for ten, calo in CALO.items()
            if calo == calo_min
        ]

        return (
            f"🌿 Nếu ưu tiên lựa chọn ít ngọt/nhẹ hơn, "
            f"bạn có thể tham khảo **{', '.join(mon_it)}**.\n\n"
            f"📊 Mức năng lượng tham khảo khoảng "
            f"**{calo_min} kcal/ly**.\n\n"
            f"💡 Bạn cũng có thể chọn mức **0% hoặc 30% đường** "
            f"khi đặt món."
        )

    # -----------------------------------------------------
    # 6. TRÀ SỮA NHIỀU CALO NHẤT
    # -----------------------------------------------------
    if (
        "nhiều calo" in q
        or "nhiều calories" in q
        or "calo cao nhất" in q
        or "calories cao nhất" in q
        or "nhiều năng lượng" in q
    ):
        calo_max = max(CALO.values())

        mon_calo_max = [
            ten for ten, calo in CALO.items()
            if calo == calo_max
        ]

        return (
            f"🔥 Theo dữ liệu tham khảo của quán, "
            f"**{', '.join(mon_calo_max)}** có mức năng lượng cao nhất, "
            f"khoảng **{calo_max} kcal/ly**.\n\n"
            f"⚠️ Lượng calo thực tế có thể thay đổi tùy theo "
            f"size, lượng đường, topping và công thức pha chế."
        )

    # -----------------------------------------------------
    # 7. HỎI MENU
    # -----------------------------------------------------
    if (
        "menu" in q
        or "có những loại" in q
        or "có trà sữa gì" in q
        or "danh sách" in q
    ):
        danh_sach = ""

        for ten, gia in TRA_SUA.items():
            danh_sach += f"• **{ten}**: {gia:,.0f} VNĐ\n"

        return (
            "🧋 **Menu trà sữa hiện tại:**\n\n"
            + danh_sach
        )

    # -----------------------------------------------------
    # 8. HỎI GIÁ
    # -----------------------------------------------------
    for ten_tra, gia in TRA_SUA.items():

        if ten_tra.lower() in q:

            return (
                f"🧋 **{ten_tra}** có giá "
                f"**{gia:,.0f} VNĐ/ly**.\n\n"
                f"📊 Năng lượng tham khảo: "
                f"**{CALO[ten_tra]} kcal/ly**."
            )

    # -----------------------------------------------------
    # 9. CHÀO HỎI
    # -----------------------------------------------------
    if (
        "xin chào" in q
        or "chào" in q
        or "hello" in q
        or "hi" in q
    ):
        return (
            "👋 Xin chào! Mình là chatbot của quán trà sữa.\n\n"
            "Bạn có thể hỏi mình:\n"
            "• Loại trà sữa nào giá cao nhất?\n"
            "• Loại nào giá thấp nhất?\n"
            "• Trà sữa matcha kèm topping nào?\n"
            "• Loại nào ít ngọt?\n"
            "• Loại nào nhiều calo?"
        )

    # -----------------------------------------------------
    # 10. KHÔNG HIỂU CÂU HỎI
    # -----------------------------------------------------
    return (
        "🤖 Mình chưa hiểu câu hỏi này.\n\n"
        "Bạn có thể thử hỏi:\n"
        "• **Loại trà sữa nào giá cao nhất?**\n"
        "• **Loại trà sữa nào giá thấp nhất?**\n"
        "• **Trà sữa matcha kèm topping nào?**\n"
        "• **Loại trà sữa nào ít ngọt?**\n"
        "• **Loại trà sữa nào nhiều calo?**"
    )


# =========================================================
# TIÊU ĐỀ
# =========================================================
st.title("🧋 QUÁN TRÀ SỮA")
st.subheader("Tính hóa đơn")

st.divider()

# =========================================================
# THÔNG TIN KHÁCH HÀNG
# =========================================================
st.header("👤 Thông tin khách hàng")

ten_khach = st.text_input(
    "Tên khách hàng",
    placeholder="Nhập tên khách hàng..."
)

# =========================================================
# CHỌN MÓN
# =========================================================
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
        [
            "0% đường",
            "30% đường",
            "50% đường",
            "70% đường",
            "100% đường"
        ]
    )

    muc_da = st.selectbox(
        "Mức độ đá",
        [
            "Không đá",
            "30% đá",
            "50% đá",
            "70% đá",
            "100% đá"
        ]
    )

    topping = st.selectbox(
        "Topping",
        list(TOPPING.keys())
    )


# =========================================================
# MÓN THÊM
# =========================================================
st.header("🍰 Món ăn thêm")

them_mon = st.checkbox("Có thêm món")

mon_them = "Không thêm món"
so_luong_mon_them = 0

if them_mon:

    col3, col4 = st.columns(2)

    with col3:

        mon_them = st.selectbox(
            "Chọn món thêm",
            [
                x for x in MON_THEM.keys()
                if x != "Không thêm món"
            ]
        )

    with col4:

        so_luong_mon_them = st.number_input(
            "Số lượng món thêm",
            min_value=1,
            max_value=20,
            value=1,
            step=1
        )


# =========================================================
# TÍNH TIỀN
# =========================================================
gia_tra = TRA_SUA[loai_tra]
gia_size = SIZE[size_ly]
gia_topping = TOPPING[topping]

tien_tra_sua = (
    gia_tra
    + gia_size
    + gia_topping
) * so_luong

if them_mon:
    tien_mon_them = (
        MON_THEM[mon_them]
        * so_luong_mon_them
    )
else:
    tien_mon_them = 0

tong_tien = tien_tra_sua + tien_mon_them


# =========================================================
# NÚT XEM HÓA ĐƠN
# =========================================================
if st.button(
    "🧾 XEM HÓA ĐƠN",
    use_container_width=True
):

    if ten_khach.strip() == "":
        st.warning(
            "⚠️ Vui lòng nhập tên khách hàng!"
        )

    else:

        st.success(
            "Đã tạo hóa đơn thành công!"
        )

        st.divider()

        # -------------------------------------------------
        # THÔNG TIN ĐƠN HÀNG
        # -------------------------------------------------
        st.header("📋 Thông tin đơn hàng")

        st.write(
            f"**Khách hàng:** {ten_khach}"
        )

        st.write(
            f"**Loại trà sữa:** {loai_tra}"
        )

        st.write(
            f"**Size:** {size_ly}"
        )

        st.write(
            f"**Số lượng:** {so_luong} ly"
        )

        st.write(
            f"**Đường:** {muc_duong}"
        )

        st.write(
            f"**Đá:** {muc_da}"
        )

        st.write(
            f"**Topping:** {topping}"
        )

        if them_mon:

            st.write(
                f"**Món thêm:** "
                f"{mon_them} × {so_luong_mon_them}"
            )

        else:

            st.write(
                "**Món thêm:** Không có"
            )

        # -------------------------------------------------
        # CHI TIẾT THANH TOÁN
        # -------------------------------------------------
        st.subheader(
            "💰 Chi tiết thanh toán"
        )

        st.write(
            f"Trà sữa: "
            f"**{tien_tra_sua:,.0f} VNĐ**"
        )

        if them_mon:

            st.write(
                f"Món thêm: "
                f"**{tien_mon_them:,.0f} VNĐ**"
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

        # -------------------------------------------------
        # LƯU HÓA ĐƠN
        # -------------------------------------------------
        st.session_state["hoa_don"] = {

            "ten_khach": ten_khach,

            "loai_tra": loai_tra,

            "so_luong": so_luong,

            "size": size_ly,

            "duong": muc_duong,

            "da": muc_da,

            "topping": topping,

            "mon_them": mon_them,

            "so_luong_mon_them":
                so_luong_mon_them,

            "tien_tra_sua":
                tien_tra_sua,

            "tien_mon_them":
                tien_mon_them,

            "tong_tien":
                tong_tien
        }


# =========================================================
# THANH TOÁN
# =========================================================
if "hoa_don" in st.session_state:

    st.divider()

    st.header("💳 Thanh toán")

    if st.button(
        "💵 THANH TOÁN",
        use_container_width=True
    ):

        hd = st.session_state["hoa_don"]

        st.success(
            "✅ Thanh toán thành công!"
        )

        st.divider()

        # -------------------------------------------------
        # HÓA ĐƠN
        # -------------------------------------------------
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
                    <b>Khách hàng:</b>
                    {hd["ten_khach"]}
                </p>

                <p>
                    <b>Thời gian:</b>
                    {datetime.now().strftime(
                        "%d/%m/%Y %H:%M:%S"
                    )}
                </p>

                <hr>

                <p>
                    <b>Trà sữa:</b>
                    {hd["loai_tra"]}
                </p>

                <p>
                    <b>Size:</b>
                    {hd["size"]}
                </p>

                <p>
                    <b>Số lượng:</b>
                    {hd["so_luong"]} ly
                </p>

                <p>
                    <b>Đường:</b>
                    {hd["duong"]}
                </p>

                <p>
                    <b>Đá:</b>
                    {hd["da"]}
                </p>

                <p>
                    <b>Topping:</b>
                    {hd["topping"]}
                </p>

                <hr>

                <p>
                    <b>Tiền trà sữa:</b>
                    {hd["tien_tra_sua"]:,.0f} VNĐ
                </p>
            </div>
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


# =========================================================
# CHATBOT
# =========================================================
st.divider()

st.header("🤖 Chatbot tư vấn trà sữa")

st.write(
    "Bạn có thể hỏi chatbot về menu, giá, topping "
    "và thông tin tham khảo về năng lượng."
)

# ---------------------------------------------------------
# GỢI Ý CÂU HỎI
# ---------------------------------------------------------
st.caption("💡 Một số câu hỏi bạn có thể thử:")

col_a, col_b = st.columns(2)

with col_a:

    st.info(
        "💰 Loại trà sữa nào giá cao nhất?"
    )

    st.info(
        "💵 Loại trà sữa nào giá thấp nhất?"
    )

    st.info(
        "🧋 Trà sữa matcha kèm topping nào?"
    )

with col_b:

    st.info(
        "🌿 Loại trà sữa nào ít ngọt?"
    )

    st.info(
        "🔥 Loại trà sữa nào nhiều calo?"
    )

    st.info(
        "📋 Quán có những loại trà sữa gì?"
    )


# ---------------------------------------------------------
# Ô NHẬP CHATBOT
# ---------------------------------------------------------
cau_hoi = st.chat_input(
    "Nhập câu hỏi về trà sữa..."
)

if cau_hoi:

    # Tin nhắn của người dùng
    with st.chat_message("user"):
        st.write(cau_hoi)

    # Câu trả lời chatbot
    tra_loi = chatbot_tra_sua(cau_hoi)

    with st.chat_message("assistant"):
        st.markdown(tra_loi)
