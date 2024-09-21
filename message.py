def remove_braces(input_str):
    result = input_str.strip('{}')
    return result.strip("''")

def format_time(pt, rt):
    print(rt, pt)
    times = [str(rt), str(pt)]
    f_t = []
    print(times)
    for time in times:
        result = remove_braces(time)
        f_t.append(result)
    print(f_t)
    f_t = [item.split(":") for item in f_t]
    print(f_t)

    f_time = []
    for rt in f_t:
        if int(rt[0]) > 12:
            f_time.append(f"{int(rt[0])-12}:{rt[1]} PM")
        elif int(rt[0]) == 12:
            f_time.append(f"{rt[0]}:{rt[1]} PM")
        elif int(rt[0]) == 0:
            f_time.append(f"{int(rt[0])+12}:{rt[1]} AM")
        else:
            f_time.append(f"{rt[0]}:{rt[1]} AM")
    result = {
        "pickup_time": f_time[1],
        "return_time": f_time[0]
    }
    return result


def company_car_form(details):
    result = format_time(pt={details["pickup_time"]}, rt={details["return_time"]})
    return f'''<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0;">
    <div style="background-color: #f8f9fa; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #333333;">New Car Rental Request!</h2>
            <p>Hello <strong>SKLP Car Rental</strong>,</p>

            <p>You have received a new car rental request from {details["name"]}. Below are the details of the request:</p>

            <ul>
                <li><strong>Name:</strong> {details["name"]}</li>
                <li><strong>Email:</strong> {details["email"]}</li>
                <li><strong>Phone:</strong> {details["phone"]}]</li>
                <li><strong>Vehicle Type:</strong> {details["car_type"]}</li>
                <li><strong>Pickup Date:</strong> {details["pickup_date"]}</li>
                <li><strong>Pickup Time:</strong> {result["pickup_time"]}</li>
                <li><strong>Return Date:</strong> {details["return_date"]}</li>
                <li><strong>Return Time:</strong> {result["return_time"]}</li>
            </ul>

            <p>Please review this request and follow up with the customer to confirm their booking and finalize the process.</p>

            <p>Best regards,</p>
            <p><strong>Python Automated System</strong></p>
        </div>
    </div>
</body>
</html>
'''

def client_car_form(details):
    result = format_time(pt={details["pickup_time"]}, rt={details["return_time"]})
    return f'''<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0;">
    <div style="background-color: #f8f9fa; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #333333;">Processing the Car Rental Request!</h2>
            <p>Dear <strong>{details["name"]}</strong>,</p>

            <p>Thank you for choosing <strong>SKLP Car Rental</strong> for your car rental needs! We have received your request and are in the process of reviewing the details. Below is a summary of your booking request:</p>

            <ul>
                <li><strong>Vehicle Type:</strong> {details["car_type"]}</li>
                <li><strong>Pickup Location:</strong> Company Location</li>
                <li><strong>Pickup Date:</strong> {details["pickup_date"]}</li>
                <li><strong>Pickup Time:</strong> {result["pickup_time"]}</li>
                <li><strong>Return Location:</strong> Company Location</li>
                <li><strong>Return Date:</strong> {details["return_date"]}</li>
                <li><strong>Return Time:</strong> {result["return_time"]}</li>
            </ul>

            <h3>Contact Details</h3>
            <ul>
                <li><strong>Name:</strong> {details["name"]}</li>
                <li><strong>Email:</strong> {details["email"]}</li>
                <li><strong>Phone:</strong> {details["phone"]}]</li>
            </ul>

            <p>If there are any issues with your booking details, or if you would like to make any changes, please reply to this email or contact us directly.</p>

            <p>Thank you once again for trusting us. We look forward to assisting you in making your journey smooth and comfortable.</p>

            <p>Best regards,</p>

            <p><strong>SKLP Car Rental</strong><br>
            +63 991 5671 299</p>
        </div>
    </div>
</body>
</html>
'''

def company_concern_form(details):
    return f'''<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0;">
    <div style="background-color: #f8f9fa; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #333333;">New Concern Raised!</h2>
            <p>Hello <strong>SKLP Car Rental</strong>,</p>

            <p>A customer has submitted a concern/request via the form on the website. Please find the details below:</p>

            <h3>Concern Details</h3>
            <ul>
                <li><strong>Customer Name:</strong> {details["name"]}</li>
                <li><strong>Email:</strong> {details["email"]}</li>
                <li><strong>Phone Number:</strong> {details["phone"]}</li>
                <li><strong>Concern:</strong> {details["concern"]}</li>
            </ul>

            <p>Please review this concern and take the appropriate action. You can reply directly to the customer using the email provided.</p>

            <p>If you have any questions or need further information, please feel free to contact the customer or reach out to our support team.</p>

            <p>Best regards,</p>

            <p><strong>Python Automated System</strong></p>
        </div>
    </div>
</body>
</html>
'''



def req_confirmation(details):
    result = format_time(pt={details["pickup_time"]}, rt={details["return_time"]})
    return f'''<html>
<body style="font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0;">

    <div style="background-color: #f8f9fa; padding: 20px;">
        <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);">
            <h2 style="color: #333333;">Car Rental Pickup Confirmation!</h2>
            <p>Dear <strong>{details["name"]}</strong>,</p>

            <p>Your car rental request has been processed successfully. Below are the details of your rental:</p>

            <ul>
                <li><strong>Car Name:</strong> {details["car_name"]}</li>
                <li><strong>Car Type:</strong> {details["car_type"]}</li>
                <li><strong>Capacity:</strong> {details["capacity"]}</li>
                <li><strong>Transmission:</strong> {details["transmission"]}</li>
                <li><strong>Gasoline:</strong> {details["gasoline"]}</li>
                <li><strong>Pickup Location:</strong> Company Location</li>
                <li><strong>Pickup Date:</strong> {details["pickup_date"]}</li>
                <li><strong>Pickup Time:</strong> {result["pickup_time"]}</li>
                <li><strong>Return Location:</strong> Company Location</li>
                <li><strong>Return Date:</strong> {details["return_date"]}</li>
                <li><strong>Return Time:</strong> {result["return_time"]}</li>
            </ul>

            <p>You may now come to the designated <a href="https://www.google.com/maps/search/8242+Ramos+Compd.+Dr.+A.+Santos+Ave+Brgy.+San+Isidro.+Sucat+Parañaque+City.+,+1700+Parañaque,+Philippines/@14.506005,120.9961652,208m/data=!3m1!1e3?hl=en&entry=ttu&g_ep=EgoyMDI0MDkxNi4wIKXMDSoASAFQAw%3D%3D">pickup location</a> on the scheduled date. Please ensure you have the necessary documents with you when you come to collect the car.</p>

            <p>If you have any further questions or changes regarding your booking, feel free to reply to this email or contact us directly.</p>

            <p>Thank you for choosing <strong>SKLP Car Rental</strong> for your car rental needs. We look forward to serving you.</p>

            <p>Safe travels!</p>

            <p>Best regards,</p>

            <p><strong>SKLP Car Rental</strong><br>
            +63 991 5671 299</p>

        </div>
    </div>

</body>
</html>
'''