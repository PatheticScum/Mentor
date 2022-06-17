from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('course_details/', course_details, name='course_details'),
    path('courses/', courses, name='courses'),
    path('events/', events, name='events'),
    path('pricing/', pricing, name='pricing'),
    path('trainers/', trainers, name='trainers'),
    path('testimonial/', testimonial, name='testimonial'),
    path('profile/', profile, name='profile'),
    path('user_form/', user_form, name='user_form'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]

# {% load static %}
#
#
# <section id="testimonials" class="testimonials">
#     <div class="container" data-aos="fade-up">
#
#         <div class="section-title">
#             <h2>Testimonials</h2>
#             <p>What are they saying</p>
#         </div>
#
#         <div class="testimonials-slider swiper" data-aos="fade-up" data-aos-delay="100">
#             <div class="swiper-wrapper">
#
#                 <div class="swiper-slide">
#                     <div class="testimonial-wrap">
#                         <div class="testimonial-item">
#                             <img src="{% static 'blog/assets/img/testimonials/testimonials-1.jpg' %}"
#                                  class="testimonial-img" alt="">
#                             {% for testimonial in testimonials %}
#                             <h4>{{ testimonial.name }}</h4>
#                             <h4>{{ testimonial.job }}</h4>
#                             {% endfor %}
#                             <p>
#                                 <i class="bx bxs-quote-alt-left quote-icon-left"></i>
#                                 Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit
#                                 rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam,
#                                 risus at semper.
#                                 <i class="bx bxs-quote-alt-right quote-icon-right"></i>
#                             </p>
#                         </div>
#                     </div>
#                 </div><!-- End testimonial item -->
#
#                 <div class="swiper-slide">
#                     <div class="testimonial-wrap">
#                         <div class="testimonial-item">
#                             <img src="{% static 'blog/assets/img/testimonials/testimonials-2.jpg' %}"
#                                  class="testimonial-img" alt="">
#                             <h3>Sara Wilsson</h3>
#                             <h4>Designer</h4>
#                             <p>
#                                 <i class="bx bxs-quote-alt-left quote-icon-left"></i>
#                                 Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid
#                                 cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet
#                                 legam anim culpa.
#                                 <i class="bx bxs-quote-alt-right quote-icon-right"></i>
#                             </p>
#                         </div>
#                     </div>
#                 </div><!-- End testimonial item -->
#
#                 <div class="swiper-slide">
#                     <div class="testimonial-wrap">
#                         <div class="testimonial-item">
#                             <img src="{% static 'blog/assets/img/testimonials/testimonials-3.jpg' %}"
#                                  class="testimonial-img" alt="">
#                             <h3>Jena Karlis</h3>
#                             <h4>Store Owner</h4>
#                             <p>
#                                 <i class="bx bxs-quote-alt-left quote-icon-left"></i>
#                                 Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam
#                                 duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.
#                                 <i class="bx bxs-quote-alt-right quote-icon-right"></i>
#                             </p>
#                         </div>
#                     </div>
#                 </div><!-- End testimonial item -->
#
#                 <div class="swiper-slide">
#                     <div class="testimonial-wrap">
#                         <div class="testimonial-item">
#                             <img src="{% static 'blog/assets/img/testimonials/testimonials-4.jpg' %}"
#                                  class="testimonial-img" alt="">
#                             <h3>Matt Brandon</h3>
#                             <h4>Freelancer</h4>
#                             <p>
#                                 <i class="bx bxs-quote-alt-left quote-icon-left"></i>
#                                 Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat
#                                 minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore
#                                 labore illum veniam.
#                                 <i class="bx bxs-quote-alt-right quote-icon-right"></i>
#                             </p>
#                         </div>
#                     </div>
#                 </div><!-- End testimonial item -->
#
#                 <div class="swiper-slide">
#                     <div class="testimonial-wrap">
#                         <div class="testimonial-item">
#                             <img src="{% static 'blog/assets/img/testimonials/testimonials-5.jpg' %}"
#                                  class="testimonial-img" alt="">
#                             <h3>John Larson</h3>
#                             <h4>Entrepreneur</h4>
#                             <p>
#                                 <i class="bx bxs-quote-alt-left quote-icon-left"></i>
#                                 Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster
#                                 veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam
#                                 culpa fore nisi cillum quid.
#                                 <i class="bx bxs-quote-alt-right quote-icon-right"></i>
#                             </p>
#                         </div>
#                     </div>
#                 </div><!-- End testimonial item -->
#
#             </div>
#             <div class="swiper-pagination"></div>
#         </div>
#
#     </div>
# </section>
