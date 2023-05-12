import multiprocessing as mp

from simoji.lib.module_executor.MyNode import MyNode
from simoji.lib.module_executor.LeaveNode import LeaveNode


class GlobalLeaveNode(LeaveNode):

    def __init__(self, name: str, parent: MyNode, result_queue: mp.Queue):

        super(GlobalLeaveNode, self).__init__(name=name, parent=parent)
        self.result_queue = result_queue
