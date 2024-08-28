from flask import jsonify, request, render_template, url_for, redirect
from ..models.review import Review
from bson.objectid import*

def review():
    if request.method == 'POST':
        # Get the review data from the request
        name = request.form.get('name')
        barber_name = request.form.get('barber_name')
        services = request.form.get('services')
        review_message = request.form.get('review_message')
        rating = int(request.form.get('rating'))
        # Prepare the review data as a dictionary
        review_data = {
            'name': name,
            'barber_name': barber_name,
            'services': services,
            'review_message': review_message,
            'rating': rating
        }
        # Save the review data to the MongoDB database
        Review.save_review(review_data)
        # Redirect to the review_display route after submission
        return redirect(url_for('rev.review_display'))

    # Render the review template on GET request
    return render_template('review.html')


def review_display():
    # Retrieve data from MongoDB
    displays = Review.get_reviews()

    # Render the review_display template with the data
    return render_template('review.html', displays=displays)
