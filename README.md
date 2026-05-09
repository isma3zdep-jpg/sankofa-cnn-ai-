# sankofa-cnn-ai-


هذا المشروع عبارة عن شبكة عصبية ذكية (Neural Network) بنيتها باستخدام بايتورش عشان تتعرف على الأرقام المكتوبة بخط اليد.

المكتبات اللي تحتاج تحملها
قبل ما تبدأ، تأكد إنك محمل المكاتب هذي عندك في الجهاز. افتح الـ Terminal واكتب:

pip install torch torchvision matplotlib

ترتيب الملفات في المجلد
عشان الكود يشتغل معك صح ومن غير "إيرورات"، لازم ملفين الكود يكونوا مع بعض في نفس المجلد:

test.py: هذا الملف هو الأساس، فيه بناء الموديل وعملية التدريب.

matplot_viz.py: هذا الملف وظيفته العرض، يسحب الموديل اللي تدرب ويوريك النتائج بشكل بصري.

طريقة التشغيل
أولاً: شغل ملف test.py. الموديل راح يبدأ يحمل البيانات من النت ويخزنها في مجلد اسمه AI ويبدأ يتدرب (بتشوف رقم الـ Epoch والـ Batch يطلع لك في الشاشة).

ثانياً: بعد ما يخلص التدريب، شغل ملف matplot_viz.py. راح تفتح لك نافذة فيها صورة الرقم الحقيقي وتوقع الذكاء الاصطناعي فوقها. إذا التوقع صح بيطلع اللون أخضر، وإذا خطأ بيطلع أحمر.

كيف تعدل على المشروع؟
إذا حاب تطور في دقة الذكاء الاصطناعي أو تغير في إعداداته، ادخل على ملف test.py وعدل في هذي القيم:

epoch: عدد مرات التدريب. زوّدها عشان الموديل يتعلم أكثر.

hiddeen_layers_n: عدد الأعصاب (Neurons) في الطبقات المخفية.

lr: سرعة التعلم، إذا شفت الموديل يتخبط صغر هذي القيمة.

تنبيه بخصوص مسار البيانات
في الكود، مسار البيانات محدد لمجلد عندي على سطح المكتب. عشان يشتغل عندك بدون مشاكل:

افتح ملف test.py.

ابحث عن سطر root=r'C:\Users\...'.

غيره وخليه root='./data' عشان المجلد ينزل عندك في نفس مكان المشروع وما يسبب لك مشاكل في الصلاحيات.















This project is a Deep Neural Network built with PyTorch designed to recognize handwritten digits from the MNIST dataset.

Prerequisites
Make sure you have the following libraries installed. You can install them via terminal using:

pip install torch torchvision matplotlib

File Structure
To ensure the code runs correctly without path errors, keep both files in the same directory:

test.py: The main script containing the model architecture and the training loop.

matplot_viz.py: The visualization script that loads the trained model and displays the results.

How to Run
Step 1: Run test.py first. The script will automatically download the MNIST dataset into a folder named AI and start the training process. You will see the Epoch and Batch numbers printed in the console.

Step 2: Once training is complete, run matplot_viz.py. A window will appear showing the actual image, the real label, and the AI's prediction.

Green Title: Correct prediction.

Red Title: Incorrect prediction.

Customization
If you want to experiment with the AI's performance, open test.py and modify these parameters:

epoch: The number of training iterations. Increasing this usually improves accuracy.

hiddeen_layers_n: The number of neurons in the hidden layers.

lr (Learning Rate): How fast the model learns. If the model is unstable, try decreasing this value.

Path Configuration Note
The current code uses a specific local path for the dataset. To make it work seamlessly on any machine:

Open test.py.

Find the line root=r'C:\Users\...'.

Change it to root='./data'. This will create a data folder within the project directory instead of looking for a specific user path.
