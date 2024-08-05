from api.models.db.cycle import Cycle
from api.models.db.key_result_check_in import KeyResultCheckIn
from api.models.db.key_result_check_mark import KeyResultCheckMark
from api.models.db.key_result_comment import KeyResultComment
from api.models.db.team import Team
from api.models.db.user import User
from api.models.db.key_result import KeyResult
from api.models.db.objective import Objective


DB_MAP = {
    'team': Team,
    'user': User,
    'cycle': Cycle,
    'objective': Objective,
    'key-result': KeyResult,
    'key-result-check-mark': KeyResultCheckMark,
    'key-result-check_in': KeyResultCheckIn,
    'key-result-comment': KeyResultComment,
}
