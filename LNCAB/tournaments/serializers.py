from rest_framework import serializers
from tournaments.models import Game


class GameSerializer(serializers.ModelSerializer):
    team_local = serializers.StringRelatedField(read_only=True)
    team_visitor = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Game
        fields = ('id','team_local','team_visitor','local_points','visitor_points',
                  'local_q1','local_q2','local_q3','local_q4','visitor_q1','visitor_q2',
                  'visitor_q3','visitor_q4','local_points','visitor_points')
