# Changelog | سجل التغييرات

## 2026-11-17 — Lesson 02: classroom word vectors and similarity

### English
- Published **Lesson 02 — How Does AI Connect Words?** in its single permanent folder `lessons/02-word-embeddings/`.
- Added learner-controlled word pairs, editable example sentences, actual co-occurrence vector counts, computed cosine similarity, nearest neighbours and a 2D projection generated from those vectors.
- Included a static, explicitly illustrative king − man + woman ≈ queen example with teaching numbers; no invented numbers are presented as trained-model outputs.
- Added English-only and Arabic-only examples according to the selected language, Arabic RTL throughout, a 25-minute teacher game and bilingual guides.
- The lightweight model is a genuine classroom calculation, **not pretrained Qwen embeddings or LLM inference**. It needs no network connection or model download.
- Updated the root homepage, both root READMEs and both teacher guides. Lesson 01 files are unchanged and are not bundled as duplicates.

### العربية
- نشر **الدرس الثاني — كيف يربط الذكاء الاصطناعي الكلمات؟** في مجلده الدائم الوحيد `lessons/02-word-embeddings/`.
- إضافة مقارنة كلمتين، وتعديل جمل الأمثلة، وحساب متجهات السياق والتشابه فعلياً، وعرض الكلمات القريبة وخريطة محسوبة ثنائية الأبعاد.
- تضمين مثال ثابت للملك والرجل والمرأة والملكة بأرقام تعليمية واضحة، دون تقديمها على أنها نتائج نموذج مدرَّب.
- دعم أمثلة عربية خاصة بالواجهة العربية واتجاه من اليمين إلى اليسار، مع دليل المعلم ونشاط مدته ٢٥ دقيقة.
- هذه تجربة حسابية تعليمية خفيفة **وليست متجهات Qwen المدرَّبة أو تشغيل نموذج لغوي كبير**.
- تحديث الصفحة الرئيسية وملفات القراءة وأدلة المعلمين مع إبقاء ملفات الدرس الأول دون تعديل أو نسخ مكرر.

---

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
