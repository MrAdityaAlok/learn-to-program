from re import sub


class PhoneNumber:
    def __init__(self, number):
        """Phone number utility class."""
        self.number = sub(r"\D+", "", number)
        length = len(self.number)

        if 11 < length < 10:
            raise ValueError(f"Invalid phone number length({length})")
        if (
            length == 11 and self.number[0] != "1"
        ):  # this question accepts +1 only
            raise ValueError(
                "Invalid country code. Should be +1 for NANP countries."
            )
        if int(self.number[-7]) < 2:
            raise ValueError("Exchange code should be in range [2-9]")

        self.area_code = self.number[-10:-7]

        if int(self.area_code[0]) < 2:
            raise ValueError("Area code should be in range [2-9]")

        self.number = self.number[-10:]

    def pretty(self):
        return f"({self.area_code})-{self.number[-7:-4]}-{self.number[-4:]}"


# Another implementation of phone number validation without specific error message
#
# from re import sub,match
#
# self.number = sub(r"\D+","",number) # [number] is input phone number
# if not match(r"^1?[2-9]\d{2,2}[2-9]\d{6,6}$", self.number):
#     raise ValueError("Error : Invalid phone number (for NANP countries)")
