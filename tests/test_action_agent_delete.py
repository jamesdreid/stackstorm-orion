# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and

# from mock import MagicMock

from orion_base_action_test_case import OrionBaseActionTestCase

from agent_delete import AgentDelete

__all__ = [
    'AgentDeleteTestCase'
]


class AgentDeleteTestCase(OrionBaseActionTestCase):
    __test__ = True
    action_cls = AgentDelete

    def test_run_connect_fail(self):
        action = self.setup_connect_fail()
        self.assertRaises(ValueError, action.run)

    def test_run_agent_fail(self):
        action = self.setup_query_blank_results()
        self.assertRaises(ValueError,
                        action.run,
                        "router1")

    def test_run(self):
        action = self.setup_agent_exists()

        expected_result = True

        result = action.run("router1")
        self.assertEqual(result, expected_result)
