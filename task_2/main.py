from task_2.base import (
    Fish,
    Mammal,
    SwimmerMixin,
    WalkerMixin,
)


class Mouse(Mammal, WalkerMixin):
    pass


class Whale(Mammal, SwimmerMixin):
    pass


class Catfish(Fish, SwimmerMixin):
    pass


class Otter(Mammal, WalkerMixin, SwimmerMixin):
    pass
