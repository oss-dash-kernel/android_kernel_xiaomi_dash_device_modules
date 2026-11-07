#
# Copyright (C) 2015 MediaTek Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#

ccflags-y += -I$(DEVICE_MODULES_PATH)/drivers/misc/mediatek/include/mt-plat/
ccflags-y += -I$(DEVICE_MODULES_PATH)/drivers/misc/mediatek/mmdebug/
ccflags-y += -I$(DEVICE_MODULES_PATH)/drivers/misc/mediatek/vcp/include/
ccflags-y += -I$(DEVICE_MODULES_PATH)/drivers/misc/mediatek/vcp/rv/
# The stub exports the same mmdebug_is_init_done symbol as the real VCP
# driver. Building both lets depmod pick the stub as the provider, and
# loading it next to the real driver fails with a duplicate-export error
# that aborts every dependent module. MT6991 has VCP, keep only the real
# driver.
obj-$(CONFIG_MTK_MMDEBUG) += mtk-mmdebug-vcp.o

