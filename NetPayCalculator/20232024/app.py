from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('NetPayCalc.html')

@app.route('/calculate', methods=['POST'])

#Global Variables
taxBracketFloors = [0, 19001, 45001, 135001, 190001]
taxRates = [0, 0.16, 0.3, 0.37, 0.45]
taxAdditions = [0, 0, 4159, 31159, 51509]
hecsRepaymentRates = [0, 1, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
hecsBracketFloors = [0, 51550, 59519, 63090, 66876, 70889, 75141, 79650, 84430, 89495, 94866, 100558, 106591, 112986, 119765, 126951, 134569, 142643, 151201]

def calculate():
    #Get user input for salary and hecs debt
    salary = float(request.form['income'],2)
    hecsDebt = float(request.form['hecsDebt'],2)
    payIncrement = request.form['payFrequency']

    #Calculate which tax and repayment brackets user is in
    n = getTaxBracket(salary)
    m = getHecsBracket(salary)

    #Calculate annual tax and hecs to be paid, then print them
    taxpaid = round(taxAdditions[n] + taxRates[n]*(salary - taxBracketFloors[n]), 2)
    hecspaid = round(hecsDebt*hecsRepaymentRates[m]/100, 2)

    print("\n")
    print("Annual tax owed: $", taxpaid)
    print("Annual HECS Debt owed: $", hecspaid)
    print("\n")

    #Calculate annual net salary, then print desired pay increment
    netAnnualSalary = round(salary - taxpaid - hecspaid, 2)
    printPay(netAnnualSalary, payIncrement, taxpaid, hecspaid)
    print("\n")

    if payIncrement == 'monthly':
        i=12
    elif payIncrement == 'fortnightly':
        i=26
    elif payIncrement == 'weekly':
        i=52
    else:
        print("error with Pay Increment selection")

    netPay = round(netAnnualSalary/i, 2)
    incTax = round(taxpaid/i, 2))
    incHecs = round(hecspaid/i, 2))

    return f"'Net Pay: ${netPay:.2f} {payIncrement}, (${incTax} Tax and ${incHecs} Hecs paid)' <br>
            'Annual Net Pay: ${netAnnualSalary}, (${taxpaid} Tax and ${hecspaid} Hecs paid)'"

    #end of main()

def getTaxBracket(salary):
    """ Takes salary input and works out which tax bracket user should be in

        Inputs: salary (float)
                    given by user in main()
        Outputs: n (int)
                    correct tax bracket to be applied
    """

    if (taxBracketFloors[0] < salary < taxBracketFloors[1]):
        n = 0
    elif (taxBracketFloors[1] < salary < taxBracketFloors[2]):
        n = 1
    elif (taxBracketFloors[2] < salary < taxBracketFloors[3]):
        n = 2
    elif (taxBracketFloors[3] < salary < taxBracketFloors[4]):
        n = 3
    elif (taxBracketFloors[4] < salary):
        n = 4
    else:
        print("Error with Salary")
    return n

def getHecsBracket(salary):
    """ Takes salary input and works out which hecs repayment bracket user should be in

        Inputs: salary (float)
                    given by user in main()
        Outputs: m (int)
                    correct repayment bracket to be applied
    """

    if (hecsBracketFloors[0] < salary < hecsBracketFloors[1]):
        m = 0
    elif (hecsBracketFloors[1] < salary < hecsBracketFloors[2]):
        m = 1
    elif (hecsBracketFloors[2] < salary < hecsBracketFloors[3]):
        m = 2
    elif (hecsBracketFloors[3] < salary < hecsBracketFloors[4]):
        m = 3
    elif (hecsBracketFloors[4] < salary < hecsBracketFloors[5]):
        m = 4
    elif (hecsBracketFloors[5] < salary < hecsBracketFloors[6]):
        m = 5
    elif (hecsBracketFloors[6] < salary < hecsBracketFloors[7]):
        m = 6
    elif (hecsBracketFloors[7] < salary < hecsBracketFloors[8]):
        m = 7
    elif (hecsBracketFloors[8] < salary < hecsBracketFloors[9]):
        m = 8
    elif (hecsBracketFloors[9] < salary < hecsBracketFloors[10]):
        m = 9
    elif (hecsBracketFloors[10] < salary < hecsBracketFloors[11]):
        m = 10
    elif (hecsBracketFloors[11] < salary < hecsBracketFloors[12]):
        m = 11
    elif (hecsBracketFloors[12] < salary < hecsBracketFloors[13]):
        m = 12
    elif (hecsBracketFloors[13] < salary < hecsBracketFloors[14]):
        m = 13
    elif (hecsBracketFloors[14] < salary < hecsBracketFloors[15]):
        m = 14
    elif (hecsBracketFloors[15] < salary < hecsBracketFloors[16]):
        m = 15
    elif (hecsBracketFloors[16] < salary < hecsBracketFloors[17]):
        m = 16
    elif (hecsBracketFloors[17] < salary < hecsBracketFloors[18]):
        m = 17
    elif (hecsBracketFloors[18] < salary):
        m = 18
    else:
        print("Error with Salary")
    return m


if __name__ == '__main__':
    app.run(debug=True)