import smbus


def main():
    CRYPTO_CAPE_EEPROM_ADDR = 0x57

    print "I did something!"
    bus = smbus.SMBus(1)    # 0 = /dev/i2c-0 (port I2C0
    bus.i2c_smbus_write_byte(CRYPTO_CAPE_EEPROM_ADDR, 0x02)
    bus.i2c_smbus_write_byte(CRYPTO_CAPE_EEPROM_ADDR, 0x00)
    bus.i2c_smbus_write_byte(CRYPTO_CAPE_EEPROM_ADDR, 0x00)
    bus.i2c_smbus_write_byte(CRYPTO_CAPE_EEPROM_ADDR, 0x00)
    bus.i2c_smbus_write_byte(CRYPTO_CAPE_EEPROM_ADDR, 0x00)
    for i in range(17):
        print str(bus.read_byte(CRYPTO_CAPE_EEPROM_ADDR))
    response


if __name__ == '__main__':
    main()
