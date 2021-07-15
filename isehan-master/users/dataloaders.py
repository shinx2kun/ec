from collections import defaultdict
from promise import Promise
from promise.dataloader import DataLoader
from users.models import ShippingInfo


class ShippingInfoLoader(DataLoader):
    def batch_load_fn(self, keys):
        info_by_user_ids = defaultdict(list)
        for info in ShippingInfo.objects.filter(user_id__in=keys).iterator():
            info_by_user_ids[info.user_id].append(info)
        return Promise.resolve(list(info_by_user_ids.get(user_id, []) for user_id in keys))


shipping_info_loader = ShippingInfoLoader()
