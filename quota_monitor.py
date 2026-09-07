import sys

try:
    from api_key import GEMINI_API_KEY
except ImportError:
    print("[ERROR] api_key.py 파일을 찾을 수 없습니다.")
    print()
    print("다음을 실행하세요:")
    print("cp api_key_example.py api_key.py")
    print("nano api_key.py")
    sys.exit(1)


def check_api_key():
    """API 키가 입력되었는지 확인"""

    if not GEMINI_API_KEY:
        print("[ERROR] API 키가 비어 있습니다.")
        print()
        print("다음을 실행하세요:")
        print("nano api_key.py")
        sys.exit(1)

    if GEMINI_API_KEY == "여기에_네_GEMINI_API_KEY를_넣어":
        print("[ERROR] 예시 API 키가 아직 수정되지 않았습니다.")
        print()
        print("다음을 실행하세요:")
        print("nano api_key.py")
        sys.exit(1)

    return True


def main():
    print("=" * 45)
    print("       GEMINI QUOTA MONITOR")
    print("=" * 45)

    check_api_key()

    # API 키 전체를 출력하지 않는다.
    masked_key = (
        GEMINI_API_KEY[:6]
        + "..."
        + GEMINI_API_KEY[-4:]
        if len(GEMINI_API_KEY) > 10
        else "***"
    )

    print()
    print("[OK] API 키 파일을 성공적으로 읽었습니다.")
    print(f"API Key: {masked_key}")
    print()
    print("다음 단계:")
    print("Gemini quota/usage 조회 기능을 연결할 준비가 되었습니다.")


if __name__ == "__main__":
    main()