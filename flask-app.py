
import os

import pop


pn = int(os.environ.get('PORT', 5000))

pop.create_app().run(host='0.0.0.0', port=pn)
