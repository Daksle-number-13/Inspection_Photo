# 모듈 라이브러리

inspection-photo 프로젝트의 재사용 가능한 모듈들을 관리합니다.

## 포함된 모듈

### CloudikeUploader

Cloudike 공유 폴더에 파일을 업로드하는 JavaScript 모듈

**위치:** `./cloudike-uploader.js`

#### 사용 방법

```javascript
import CloudikeUploader from './modules/cloudike-uploader.js';

const uploader = new CloudikeUploader({
  onProgress: (current, total) => console.log(`${current}/${total}`),
  onError: (index, error) => console.error(error)
});

await uploader.uploadFile(file, shareUrl, folderPath, fileName);
```

#### 주요 API

- **`uploadFile(file, shareUrl, folderPath, fileName)`** - 단일 파일 업로드
- **`uploadMultiple(files, shareUrl, folderPath, onProgress?)`** - 다중 파일 업로드

#### 완전한 문서

자세한 사용법은 프로젝트 루트의 `CLOUDIKE_UPLOADER_README.md`를 참고하세요.

---

## 다른 프로젝트에서 사용

### Git Submodule 방식 (권장)

```bash
git submodule add --depth 1 https://github.com/Daksle-number-13/inspection-photo.git inspection-photo-modules
```

그 후 필요한 모듈만 복사:

```javascript
import CloudikeUploader from './inspection-photo-modules/modules/cloudike-uploader.js';
```

### 파일 복사 방식

```bash
cp inspection-photo/modules/cloudike-uploader.js ./your-project/
```

---

## 향후 모듈 추가

새로운 재사용 가능한 기능이 생기면 여기에 추가될 예정입니다:

- 이미지 처리 모듈
- 폼 검증 모듈
- 데이터 변환 유틸리티
- 등등...

---

**개발자:** Park Jin-su (@daksle-number-13)
