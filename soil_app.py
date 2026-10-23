import streamlit as st

st.set_page_config(page_title="Soil Analysis System", page_icon="🌱", layout="centered")

st.title("🌱 نظام تحليل جودة التربة والتقييم الزراعي المتقدم")
st.write("مرحباً بك! أدخل قراءات عينة التربة الحقلية والمعملية للحصول على تقييم شامل:")

# تقسيم الشاشة لمدخلات منظمة
col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("درجة الحموضة (pH)", min_value=0.0, max_value=14.0, value=7.0)
    ec = st.number_input("الملوحة (EC - dS/m)", min_value=0.0, max_value=50.0, value=1.5)
    sar = st.number_input("نسبة امتصاص الصوديوم (SAR)", min_value=0.0, max_value=50.0, value=5.0)

with col2:
    nitrogen = st.number_input("النيتروجين (N - ppm)", min_value=0.0, max_value=1000.0, value=25.0)
    phosphorus = st.number_input("الفسفور (P - ppm)", min_value=0.0, max_value=500.0, value=15.0)
    potassium = st.number_input("البوتاسيوم (K - ppm)", min_value=0.0, max_value=1000.0, value=150.0)

# زر التحليل
if st.button("🚀 تشغيل التقرير الزراعي الشامل", use_container_width=True):
    st.markdown("---")
    st.subheader("📊 تقرير التوصيات والإدارة الزراعية:")
    
    # 1. الحموضة
    if ph < 6.0:
        st.warning(f"⚠️ الحموضة (pH = {ph}): التربة حمضية، يوصى بإضافة الجير الزراعي.")
    elif 6.0 <= ph <= 7.5:
        st.success(f"✅ الحموضة (pH = {ph}): مثالية ومتوازنة لامتصاص العناصر.")
    else:
        st.error(f"⚠️ الحموضة (pH = {ph}): قلوية مرتفعة، يوصى بإضافة كبريت زراعي.")
        
    # 2. الملوحة
    if ec < 2.0:
        st.success(f"✅ الملوحة (EC = {ec}): آمنة تماماً ولا تشكل أي خطورة.")
    else:
        st.warning(f"⚠️ الملوحة (EC = {ec}): مرتفعة نسبياً، يوصى بتحسين الصرف وغسيل التربة.")

    # 3. المغذيات
    st.markdown("### 🧪 حالة المغذيات الكبرى (N-P-K):")
    st.info(f"- النيتروجين: {nitrogen} ppm ({'منخفض ⚠️' if nitrogen < 20 else 'مناسب وجيد ✅'})")
    st.info(f"- الفسفور: {phosphorus} ppm ({'يحتاج دعم لتنشيط الجذور ⚠️' if phosphorus < 15 else 'مستوى كافٍ ✅'})")
    st.info(f"- البوتاسيوم: {potassium} ppm ({'يحتاج تسميد بوتاسي ⚠️' if potassium < 120 else 'ممتاز وجودة ثمار عالية ✅'})")