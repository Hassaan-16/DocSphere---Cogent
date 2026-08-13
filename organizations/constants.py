ORGANIZATION_FIELDS = [
    "id",
    "org_name",
    "created_at",
    "updated_at",
    "subscription_status",
    "current_plan_name",
    "current_period_end",
]

ORGANIZATION_READ_ONLY_FIELDS = ["id", "created_at", "updated_at"]

ORGANIZATION_SUBSCRIPTION_FIELDS = [
    "id",
    "org_name",
    "subscription_status",
    "current_plan_name",
    "current_period_end",
]

ORGANIZATION_SUBSCRIPTION_READ_ONLY_FIELDS = ["id", "org_name"]
