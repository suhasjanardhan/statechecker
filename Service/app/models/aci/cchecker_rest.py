import os
import logging
from ..rest import Rest
from ..rest import api_register
from ..rest import api_route
from flask import jsonify
import utils
import sys
import platform 
import subprocess

logger = logging.getLogger(__name__)

@api_register(path="/aci/cc")
class ConsistencyChecker(Rest):

    META_ACCESS = {
        "create": False,
        "read": False,
        "update": False,
        "delete": False,
    }
    
    @api_route(path="runcc", methods=["GET"])
    def runcc():
	logger.debug("running runcc definition")
	return jsonify({"success":True, "test_str":"hello world!"})
    
    @api_route(path="run_analyzer", methods=["POST"])
    def run_analyzer():
	logger.debug("running analyzer")
	cmd = "python /tmp/obj_collector_statechecker/obj_store_sc_api.py /tmp/obj_collector_statechecker/obj_collector_sc.json"
	logger.debug("run cmd: \"%s\"", cmd)
	try:
	    out = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
	    logger.debug(out)
	except subprocess.CalledProcessError as e:
	    logger.warn("error executing command: %s", e)
	    logger.warn("stderr:\n%s", e.output)
	return jsonify({"ret_val":True, "sample_str":platform.system(), "ret_str":"running analyzer"})
    
    @api_route(path="run_consumer", methods=["POST"])
    def run_obj_collector():
	logger.debug("running consumer")
	cmd = "python /tmp/obj_collector_statechecker/obj_store_sc_api.py /tmp/obj_collector_statechecker/obj_collector_sc.json"
	logger.debug("run cmd: \"%s\"", cmd)
	try:
	    out = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
	    logger.debug(out)
	except subprocess.CalledProcessError as e:
	    logger.warn("error executing command: %s", e)
	    logger.warn("stderr:\n%s", e.output)
	return jsonify({"ret_val":True, "sample_str":platform.system(), "ret_str":"running consumer"})
    
    @api_route(path="obj_collector", methods=["POST"])
    def run_obj_collector():
	logger.debug("running object collector")
	cmd = "python /tmp/obj_collector_statechecker/obj_store_sc_api.py /tmp/obj_collector_statechecker/obj_collector_sc.json"
	logger.debug("run cmd: \"%s\"", cmd)
	try:
	    out = subprocess.check_output(cmd,shell=True,stderr=subprocess.STDOUT)
	    logger.debug(out)
	except subprocess.CalledProcessError as e:
	    logger.warn("error executing command: %s", e)
	    logger.warn("stderr:\n%s", e.output)
	return jsonify({"ret_val":True, "sample_str":platform.system()})

		
