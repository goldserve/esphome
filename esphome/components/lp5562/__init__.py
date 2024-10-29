import esphome.codegen as cg
from esphome.components import i2c
import esphome.config_validation as cv
from esphome.const import CONF_ID

CODEOWNERS = ["@ssieb"]
DEPENDENCIES = ["i2c"]
MULTI_CONF = True

lp5562_ns = cg.esphome_ns.namespace("lp5562")
LP5562 = lp5562_ns.class_("LP5562", cg.Component, i2c.I2CDevice)

CONF_LP5562_ID = "lp5562_id"

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(LP5562),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(i2c.i2c_device_schema(0x30))
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await i2c.register_i2c_device(var, config)
