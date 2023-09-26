class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        true_email = set()
        n = len(emails)
        for i in range(n):
            local, domain = emails[i].split("@")
            if "." in local:
                local = local.replace(".", "")
            if "+" in local:
                m = local.find("+")
                local = local[:m]
            email_new = local + "@" + domain
            true_email.add(email_new)
        return len(true_email)