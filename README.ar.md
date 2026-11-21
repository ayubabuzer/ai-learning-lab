# مختبر تعلم الذكاء الاصطناعي | AI Learning Lab

**[English](README.md) · [الموقع](https://ayubabuzer.github.io/ai-learning-lab/)**

موقع تعليمي مجاني ومفتوح المصدر لجميع الأعمار. نبدأ بكلمات بسيطة ثم نقدّم المصطلحات التقنية بعد فهم الفكرة. الدروس ٠١–٠٥ بالعربية والإنجليزية وتعمل في المتصفح دون تنزيل نموذج كبير أو مفتاح API. الدرس ٠٦ مشروع توأم رقمي بنموذج لغوي حقيقي، **بالإنجليزية فقط**.

## مسار الدروس

| الدرس | السؤال البسيط | نوع التجربة |
|---|---|---|
| [٠١ · كيف يقرأ الذكاء الاصطناعي كلماتنا؟](lessons/01-how-ai-reads-words/) | كيف تتحول الرسالة إلى أرقام؟ | أرقام Unicode حقيقية للحروف وتقسيم مبسط للنص، وليس مُقسّم نموذج مدرب |
| [٠٢ · كيف يربط الكلمات؟](lessons/02-word-embeddings/) | كيف ترتبط الكلمات بالأرقام؟ | متجهات محسوبة من أمثلة قابلة للتعديل وقصة مصورة عن الانتباه دون نسب مخترعة |
| [٠٣ · كيف يتعلم التنبؤ؟](lessons/03-next-word-prediction/) | كيف تغيّر الأمثلة التنبؤ؟ | **علّم → اختبر → غيّر → أعد التعليم** ثم تحدٍّ اختياري لأمثلة مضللة |
| [٠٤ · كيف يتذكر؟](lessons/04-ai-context-memory/) | من أين تأتي الذاكرة؟ | تجميع حقيقي لسجل الرسائل وحذف الرسائل من الطلب؛ دون ردود مولدة |
| [٠٥ · كيف يستخدم الأدوات ويعمل لهدف؟](lessons/05-ai-retrieval/) | ما الفرق بين سير العمل والوكيل؟ | قصة مرئية واضحة، وليست تشغيل أدوات حقيقية أو وكيل مباشر |
| [٠٦ · ابنِ توأمك الرقمي](lessons/06-digital-twin/) | كيف أبني روبوت محادثة حقيقياً؟ | تطبيق Gradio بنموذج لغوي حقيقي؛ بالإنجليزية فقط |

كل درس يتبع: **شرح قصير ← تجربة أو مثال مرئي مفيد ← تغيير ← اكتشاف ← ربط بالدرس التالي**.

## تشغيل التوأم الرقمي

```bash
git clone https://github.com/ayubabuzer/ai-learning-lab.git
cd ai-learning-lab/lessons/06-digital-twin/gradio-app
uv run app.py
```

قد يكون النموذج بطيئاً محلياً. للنشر الاختياري اتبع [الدليل الكامل بالإنجليزية](lessons/06-digital-twin/gradio-app/README.md) لإنشاء حساب Hugging Face ورمز وصول خاص، ثم تسجيل الدخول عبر `uvx hf auth login` والنشر بواسطة `uv run python deploy.py`. لا تضع الرموز السرية أو البيانات الشخصية في ملفات عامة. التوأم الرقمي **روبوت محادثة لا وكيل مستقل**. لم يُتحقق من النشر المباشر في هذا الإصدار.

**المجلدات:** نحتفظ بالمجلدات الستة نفسها، بما فيها الاسم القديم `05-ai-retrieval` لتجنب كسر الروابط؛ تغيّر محتواه إلى الأدوات وسير العمل والوكلاء. لا تنشئ مجلداً إضافياً.


## Safe deployment / النشر الآمن

Use `uv run python deploy.py` from `lessons/06-digital-twin/gradio-app`. It sends only the required app source files, not `.venv` or secrets. Create a Hugging Face Write token first, authenticate using `uvx hf auth login`, then open the Space URL printed by the script. The first run asks for a Space name; subsequent runs update it. An existing oversized Space may require a clean new Space name.
