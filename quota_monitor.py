from api_key import GEMINI_API_KEY


def mask_key(key):
    """API 키를 일부만 보여준다."""
    if not key:
        return "(없음)"

    if len(key) <= 10:
        return "*" * len(key)

    return key[:6] + "..." + key[-4:]


def check_key():
    """API 키가 파일에 제대로 들어있는지 확인한다."""
    if not GEMINI_API_KEY:
        return False

    if not isinstance(GEMINI_API_KEY, str):
        return False

    if not GEMINI_API_KEY.strip():
        return False

    return True


def show_info():
    print("=" * 50)
    print("           Gemini Quota Monitor")
    print("=" * 50)
    print()

    if not check_key():
        print("❌ API 키를 찾을 수 없습니다.")
        print()
        print("api_key.py를 확인하세요.")
        return

    print("✅ API 키 파일 확인 완료")
    print(f"🔑 Key: {mask_key(GEMINI_API_KEY)}")
    print()

    print("📊 Gemini API 제한 종류")
    print("   RPM : 분당 요청 수")
    print("   TPM : 분당 토큰 수")
    print("   RPD : 일일 요청 수")
    print()

    print("⚠️ 현재 상태")
    print("   API 키 자체만으로는")
    print("   정확한 '남은 RPD/RPM/TPM'을")
    print("   공식적으로 직접 조회할 수 없습니다.")
    print()

    print("ℹ️ 이 프로그램은 quota 확인을 위해")
    print("   Gemini 생성 요청을 보내지 않습니다.")
    print()

    print("🔐 API Key:")
    print(f"   {mask_key(GEMINI_API_KEY)}")
    print()

    print("=" * 50)


if __name__ == "__main__":
    show_info()