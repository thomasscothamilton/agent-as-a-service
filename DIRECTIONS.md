# Define the base API URL
API_URL="http://localhost:8080"

# Step 1: Create the Worker Agent
WORKER_AGENT_ID=$(curl -s -X POST "$API_URL/agents" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Worker Agent",
        "role": "worker",
        "model_type": "GPT-4",
        "system_message": "Handles task execution"
    }' | jq -r '.agent_id')

echo "Worker Agent created with ID: $WORKER_AGENT_ID"

# Step 2: Create the Feedback/Approver Agent
FEEDBACK_AGENT_ID=$(curl -s -X POST "$API_URL/agents" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Feedback Agent",
        "role": "approver",
        "model_type": "GPT-4",
        "system_message": "Provides feedback and approves tasks"
    }' | jq -r '.agent_id')

echo "Feedback Agent created with ID: $FEEDBACK_AGENT_ID"

# Step 3: Create the Team
TEAM_ID=$(curl -s -X POST "$API_URL/teams" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Development Team",
        "description": "Handles all development tasks"
    }' | jq -r '.team_id')

echo "Team created with ID: $TEAM_ID"

# Step 4: Create a Task and Assign It to the Team
TASK_ID=$(curl -s -X POST "$API_URL/tasks" \
    -H "Content-Type: application/json" \
    -d '{
        "name": "Implement Feature X",
        "description": "Develop and deliver Feature X",
        "assigned_team_id": '$TEAM_ID',
        "priority": "high"
    }' | jq -r '.task_id')

echo "Task created with ID: $TASK_ID"

# Step 5: Assign the Worker Agent to the Task
curl -s -X POST "$API_URL/tasks/$TASK_ID/assign-agent" \
    -H "Content-Type: application/json" \
    -d '{
        "agent_id": '$WORKER_AGENT_ID',
        "role_in_task": "executor"
    }'

echo "Worker Agent assigned to Task"

# Step 6: Assign the Feedback/Approver Agent to the Task
curl -s -X POST "$API_URL/tasks/$TASK_ID/assign-agent" \
    -H "Content-Type: application/json" \
    -d '{
        "agent_id": '$FEEDBACK_AGENT_ID',
        "role_in_task": "approver"
    }'

echo "Feedback/Approver Agent assigned to Task"
