class ICICI:
    bank_name = "ICICI"
    homeloan_roi = 10
    sb_roi = 10
    @staticmethod
    def homeloan(amount, years):
        interest_amount = round(amount * (ICICI.homeloan_roi / 100) * years,0)
        amt_to_be_paid = amount + interest_amount
        monthly_interest = round(amt_to_be_paid / years / 12, 0)
        return SBI.homeloan_roi, amt_to_be_paid, monthly_interest


class SBI:
    bank_name = "SBI"
    homeloan_roi = 8
    sb_roi = 10
    @staticmethod
    def homeloan(amount, years):
        interest_amount = round(amount * (SBI.homeloan_roi / 100) * years,0)
        amt_to_be_paid = amount + interest_amount
        monthly_interest = round(amt_to_be_paid / years / 12, 0)
        return SBI.homeloan_roi, amt_to_be_paid, monthly_interest


class CustomerSupport(ICICI, SBI):
    @staticmethod
    def homeloan_query():
        banks = [SBI, ICICI]
        amount = int(input("Enter the loan amount : "))
        years = int(input("Enter the number of years : "))
        print(f"""Dear Customer,
Here is the comparision for your homeloan request from various banks""")
        int_comparison = []
        for bank in banks:
            print(f"Bank Name : {bank.bank_name}")
            print(f"Loan Amount : {amount}")
            print(f"Number of Years : {years}")
            roi, amt_to_be_paid, monthly_interest = bank.homeloan(amount, years)
            print(f"ROI : {roi}")
            print(f"Amount to be paid by the end of loan period : {amt_to_be_paid}")
            print(f"Monthly Interest : {monthly_interest}")
            print('*'*75)
            int_comparison.append((bank.bank_name, amt_to_be_paid))
        print("Preference Order : ")
        print(*sorted(int_comparison, key=lambda item: item[-1]), sep='\n')


# cust1 = CustomerSupport()
# cust1.homeloan_query()
# CustomerSupport.homeloan_query()


list1 = [10, 20, 30]

list.append(list1, 40)
list1.append()
