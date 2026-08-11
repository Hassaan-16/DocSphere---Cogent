from django.apps import apps


class OrganizationResolver:
    @staticmethod
    def resolve(org_input):
        Organization = apps.get_model("organizations", "Organization")

        if isinstance(org_input, Organization):
            return org_input
        if isinstance(org_input, int):
            return Organization.objects.get(pk=org_input)
        if isinstance(org_input, str):
            return Organization.objects.get_or_create(org_name=org_input)[0]
        raise ValueError(f"Invalid org input: {type(org_input)}")
