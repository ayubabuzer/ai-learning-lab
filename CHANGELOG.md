# Changelog | سجل التغييرات

## 2026-11-17 — Lesson 01 clarity and language-specific examples

### English
- Simplified the pupil-facing inspector: show the selected piece and its classroom ID, with a short explanation.
- Removed piece-type labels, decimal UTF-8 byte values and hexadecimal output from the lesson interface.
- English mode now offers English example sentences and English classroom challenges only; Arabic mode offers Arabic examples and Arabic challenges only.
- Preserved Arabic right-to-left layout, original text reconstruction and edit/compare interactions.
- Updated both READMEs, teacher guides and homepage together. No new lesson folders were created.
- This is still a simplified classroom tokenizer, not Qwen or a pretrained AI model.

### العربية
- تبسيط عرض نتائج الدرس الأول: إظهار الجزء المختار ورقمه التعليمي مع شرح قصير.
- إزالة نوع الجزء وأرقام بايتات UTF-8 والتفاصيل بالنظام الست عشري من واجهة التلاميذ.
- أمثلة عربية وأنشطة عربية فقط في الواجهة العربية، وأمثلة إنجليزية وأنشطة إنجليزية فقط في الواجهة الإنجليزية.
- الحفاظ على الاتجاه من اليمين إلى اليسار، وإعادة تركيب النص، ومقارنة النتائج قبل التعديل وبعده.
- تحديث الصفحة الرئيسية وملفات القراءة وأدلة المعلم دون إنشاء مجلدات مكررة.
- ما زالت التجربة مُقسِّماً تعليمياً مبسطاً، وليست نموذج Qwen أو نموذجاً مدرّباً.

---

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
