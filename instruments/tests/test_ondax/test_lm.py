#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Unit tests for the Ondax Laser Module
"""

# IMPORTS #####################################################################

from __future__ import absolute_import

from nose.tools import raises

import quantities

from instruments import ondax
from instruments.tests import expected_protocol

# TESTS #######################################################################


def test_acc_target():
    with expected_protocol(
            ondax.LM,
            [
                "rstli?"
            ],
            [
                "100"
            ],
            sep="\r"
    ) as lm:
        assert lm.acc.target == 100 * quantities.mA


def test_acc_enable():
    with expected_protocol(
            ondax.LM,
            [
                "lcen"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.acc.enabled = True
        assert lm.acc.enabled


def test_acc_disable():
    with expected_protocol(
            ondax.LM,
            [
                "lcdis"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.acc.enabled = False
        assert not lm.acc.enabled


@raises(TypeError)
def test_acc_enable_not_boolean():
    with expected_protocol(
            ondax.LM,
            [],
            [],
            sep="\r"
    ) as lm:
        lm.acc.enabled = "foobar"


def test_acc_on():
    with expected_protocol(
            ondax.LM,
            [
                "lcon"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.acc.on()


def test_acc_off():
    with expected_protocol(
            ondax.LM,
            [
                "lcoff"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.acc.off()


def test_apc_target():
    with expected_protocol(
            ondax.LM,
            [
                "rslp?"
            ],
            [
                "100"
            ],
            sep="\r"
    ) as lm:
        assert lm.apc.target == 100 * quantities.mW


def test_apc_enable():
    with expected_protocol(
            ondax.LM,
            [
                "len"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.apc.enabled = True
        assert lm.apc.enabled


def test_apc_disable():
    with expected_protocol(
            ondax.LM,
            [
                "ldis"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.apc.enabled = False
        assert not lm.apc.enabled


@raises(TypeError)
def test_apc_enable_not_boolean():
    with expected_protocol(
            ondax.LM,
            [],
            [],
            sep="\r"
    ) as lm:
        lm.apc.enabled = "foobar"



def test_apc_start():
    with expected_protocol(
            ondax.LM,
            [
                "sps"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.apc.start()


def test_apc_stop():
    with expected_protocol(
            ondax.LM,
            [
                "cps"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.apc.stop()


def test_modulation_on_time():
    with expected_protocol(
            ondax.LM,
            [
                "stsont?",
                "stsont:20.0"
            ],
            [
                "10",
                "OK"
            ],
            sep="\r"
    ) as lm:
        assert lm.modulation.on_time == 10 * quantities.ms
        lm.modulation.on_time = 20 * quantities.ms


def test_modulation_off_time():
    with expected_protocol(
            ondax.LM,
            [
                "stsofft?",
                "stsofft:20.0"
            ],
            [
                "10",
                "OK"
            ],
            sep="\r"
    ) as lm:
        assert lm.modulation.off_time == 10 * quantities.ms
        lm.modulation.off_time = 20 * quantities.ms


def test_modulation_enabled():
    with expected_protocol(
            ondax.LM,
            [
                "stm"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.modulation.enabled = True
        assert lm.modulation.enabled


def test_modulation_disabled():
    with expected_protocol(
            ondax.LM,
            [
                "ctm"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.modulation.enabled = False
        assert not lm.modulation.enabled


@raises(TypeError)
def test_modulation_enable_not_boolean():
    with expected_protocol(
            ondax.LM,
            [],
            [],
            sep="\r"
    ) as lm:
        lm.modulation.enabled = "foobar"


def test_tec_current():
    with expected_protocol(
            ondax.LM,
            [
                "rti?"
            ],
            [
                "100"
            ],
            sep="\r"
    ) as lm:
        assert lm.tec.current == 100 * quantities.mA


def test_tec_target():
    with expected_protocol(
            ondax.LM,
            [
                "rstt?"
            ],
            [
                "22"
            ],
            sep="\r"
    ) as lm:
        assert lm.tec.target == 22 * quantities.degC


def test_tec_enable():
    with expected_protocol(
            ondax.LM,
            [
                "tecon"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.tec.enabled = True
        assert lm.tec.enabled


def test_tec_disable():
    with expected_protocol(
            ondax.LM,
            [
                "tecoff"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.tec.enabled = False
        assert not lm.tec.enabled


@raises(TypeError)
def test_tec_enable_not_boolean():
    with expected_protocol(
            ondax.LM,
            [],
            [],
            sep="\r"
    ) as lm:
        lm.tec.enabled = "foobar"


def test_firmware():
    with expected_protocol(
            ondax.LM,
            [
                "rsv?"
            ],
            [
                "3.27"
            ],
            sep="\r"
    ) as lm:
        assert lm.firmware == "3.27"


def test_current():
    with expected_protocol(
            ondax.LM,
            [
                "rli?",
                "slc:100.0"
            ],
            [
                "120",
                "OK"
            ],
            sep="\r"
    ) as lm:
        assert lm.current == 120 * quantities.mA
        lm.current = 100 * quantities.mA


def test_maximum_current():
    with expected_protocol(
            ondax.LM,
            [
                "rlcm?",
                "smlc:100.0"
            ],
            [
                "120",
                "OK"
            ],
            sep="\r"
    ) as lm:
        assert lm.maximum_current == 120 * quantities.mA
        lm.maximum_current = 100 * quantities.mA


def test_power():
    with expected_protocol(
            ondax.LM,
            [
                "rlp?",
                "slp:100.0"
            ],
            [
                "120",
                "OK"
            ],
            sep="\r"
    ) as lm:
        assert lm.power == 120 * quantities.mW
        lm.power = 100 * quantities.mW


def test_serial_number():
    with expected_protocol(
            ondax.LM,
            [
                "rsn?"
            ],
            [
                "B099999"
            ],
            sep="\r"
    ) as lm:
        assert lm.serial_number == "B099999"


def test_status():
    with expected_protocol(
            ondax.LM,
            [
                "rlrs?"
            ],
            [
                "1"
            ],
            sep="\r"
    ) as lm:
        assert lm.status == lm.Status(1)


def test_temperature():
    with expected_protocol(
            ondax.LM,
            [
                "rtt?",
                "stt:40.0"
            ],
            [
                "35",
                "OK"
            ],
            sep="\r"
    ) as lm:
        assert lm.temperature == 35 * quantities.degC
        lm.temperature = 40 * quantities.degC


def test_enable():
    with expected_protocol(
            ondax.LM,
            [
                "lon"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.enabled = True
        assert lm.enabled


def test_disable():
    with expected_protocol(
            ondax.LM,
            [
                "loff"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.enabled = False
        assert not lm.enabled


@raises(TypeError)
def test_enable_not_boolean():
    with expected_protocol(
            ondax.LM,
            [],
            [],
            sep="\r"
    ) as lm:
        lm.enabled = "foobar"


def test_save():
    with expected_protocol(
            ondax.LM,
            [
                "ssc"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.save()


def test_reset():
    with expected_protocol(
            ondax.LM,
            [
                "reset"
            ],
            [
                "OK"
            ],
            sep="\r"
    ) as lm:
        lm.reset()
