
import os

import pop


pn = int(os.environ.get('PORT', 5000))

pop.create_bot(True).run(host='0.0.0.0', port=pn)
