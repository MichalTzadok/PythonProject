from app.routes import user_action_router
import matplotlib.pyplot as plt
from app.services import user_action_service, user_service


async def get_user_monthly_sums(user_id: int, year: int):
    await user_service.get_user_by_id(user_id)
    months = list(range(1, 13))
    monthly_sums = []
    for m in months:
        user_actions = await user_action_router.get_user_actions_by_month(user_id, year, m)
        total_sum = sum(-u.amount if u.type == 'revenue' else u.amount for u in user_actions)
        monthly_sums.append(total_sum)
    return months, monthly_sums


def create_plot(month, sums):
    plt.figure()
    plt.plot(month, sums)
    plt.xlabel('Month')
    plt.ylabel('Sum')
    plt.title('User Monthly Sums')
    plt.grid(True)
    plt.tight_layout()
    return plt.show()

async def get_user_monthly_by_type(user_id: int, action_type: str):
    await user_service.get_user_by_id(user_id)
    months = list(range(1, 13))
    monthly_amounts = []
    for month in months:
        actions_filtered = await user_action_service.get_user_actions_by_type_in_month(user_id, action_type, month)
        total_amounts = sum(-action.amount if action.type == 'expense' else action.amount for action in actions_filtered)
        monthly_amounts.append(total_amounts)
    return months, monthly_amounts



