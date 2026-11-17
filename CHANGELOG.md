# Changelog | سجل التغييرات

## 2026-11-17 — Lightweight Lesson 01 classroom release

### English
- Replaced the unreliable real-tokenizer loading step with a self-contained classroom text-to-numbers experiment for normal school computers.
- Clearly labelled the experience as **not Qwen**; classroom piece IDs are local labels, while UTF-8 byte values are genuine.
- Added click-to-inspect pieces, English/Arabic examples, RTL layout, before/after comparison, three classroom missions and a teacher guide.
- Preserved the existing homepage visual design and updated root READMEs and teacher guides.
- Packaged only the permanent `lessons/01-how-ai-reads-words/` folder; other historical folders are not bundled or deleted.
- Planned lessons 02–06 remain unpublished. Browser tests are documented in the release report; GitHub Pages deployment is not yet verified.

### العربية
- استبدال تحميل المُقسِّم السابق بتجربة تعليمية خفيفة تعمل مباشرة على الحواسيب المدرسية المعتادة.
- توضيح أن التجربة **ليست Qwen** وأن المعرّفات محلية، بينما بايتات UTF-8 المعروضة حقيقية.
- إضافة أجزاء قابلة للنقر وأمثلة عربية وإنجليزية واتجاه RTL ومقارنة قبل التعديل وبعده وثلاث مهام صفية ودليل للمعلم.
- الحفاظ على تصميم الصفحة الرئيسية وتحديث ملفات القراءة وأدلة المعلمين.
- تضمين مجلد دائم واحد للدرس الأول فقط دون حذف المجلدات القديمة تلقائياً.
- الدروس من ٠٢ إلى ٠٦ ما زالت مخططة ولم تُنشر. لم يُتحقق بعد من نشر GitHub Pages.

---

## Earlier development history

Prior releases explored Qwen tokenizer integration and Arabic readability, but live tokenizer loading was not fully verified and its presentation caused problems in practice. The lightweight release above supersedes those prototypes without misrepresenting its outputs as pretrained-model results.
